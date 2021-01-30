import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import *
from datetime import datetime
from datetime import date
from dateutil.parser import parse
import sqlite3


class MainApp:
    def __init__(self, parent, sel_company_multi_query):
        self.parent = parent
        self.conn = None
        self.curs = None

        self.act_week = None
        self.act_year = None
        self.act_day = None
        self.create_load_id = None
        self.week_var = tk.StringVar()
        self.week_var.set("")
        self.year_var = tk.StringVar()
        self.year_var.set("")
        self.weekday_var = tk.StringVar()
        self.weekday_var.set("")
        self.create_load_id_var = tk.StringVar()
        self.create_load_id_var.set("")
        self.comment_var = tk.StringVar()
        self.comment_var.set("")

        self.act_week2 = None
        self.act_year2 = None
        self.act_day2 = None
        self.create_load_id2 = None
        self.week_var2 = tk.StringVar()
        self.week_var2.set("")
        self.year_var2 = tk.StringVar()
        self.year_var2.set("")
        self.weekday_var2 = tk.StringVar()
        self.weekday_var2.set("")
        self.create_load_id_var2 = tk.StringVar()
        self.create_load_id_var2.set("")
        self.comment_var2 = tk.StringVar()
        self.comment_var2.set("")
        self.message_var = tk.StringVar()
        self.message_var.set("")

        self.data_s = None
        self.delete_box = None
        self.selected = None
        self.tree_values = None
        self.values = None

        self.sel_year_multi_query = None
        self.sel_week_multi_query = None
        self.sel_cal_multi_query = None
        self.sel_multi_id_multi_query = None
        self.sel_store_multi_query = None
        self.sel_company_multi_query = sel_company_multi_query

        self.mainframe = ttk.Frame(self.parent, style="C.TFrame")
        self.mainframe.grid(row=0, column=0)

        # Main Selection frame
        self.selection_frame1 = ttk.Frame(self.mainframe, relief="groove", style="B.TFrame")
        self.selection_frame1.grid(row=0, column=0, padx=2, pady=5, sticky="W, E")

        # Selection sub frame 1
        self.selection_sub_frame11 = ttk.Frame(self.selection_frame1, relief="flat", style="B.TFrame")
        self.selection_sub_frame11.grid(row=0, column=0, padx=2, rowspan=2, pady=2, sticky="W, E")

        # Selection sub frame 2
        self.selection_sub_frame12 = ttk.Frame(self.selection_frame1, relief="flat", style="B.TFrame")
        self.selection_sub_frame12.grid(row=0, column=1, padx=2, pady=2, sticky="W, E")

        # Selection sub frame 3
        self.selection_sub_frame13 = ttk.Frame(self.selection_frame1, relief="flat", style="B.TFrame")
        self.selection_sub_frame13.grid(row=1, column=1, padx=2, pady=2, sticky="W, N")

        # Tree frame
        self.tree_frame = ttk.Frame(self.mainframe, relief="flat", style="B.TFrame")
        self.tree_frame.grid(row=2, column=0, padx=2, pady=2, sticky="W, N")

        # Queries frame 1
        self.query_frame1 = ttk.Frame(self.mainframe, relief="groove", style="B.TFrame")
        self.query_frame1.grid(row=4, column=0, padx=2, pady=2, sticky="W, E")

        # Queries frame 2
        self.query_frame2 = ttk.Frame(self.mainframe, relief="groove", style="B.TFrame")
        self.query_frame2.grid(row=3, column=0, padx=2, pady=2, sticky="W, E")

        # Queries frame 3
        self.query_frame3 = ttk.Frame(self.mainframe, relief="groove", style="B.TFrame")
        self.query_frame3.grid(row=5, column=0, padx=2, pady=5, sticky="W, E")

        # Styles
        self.style = ttk.Style()
        # self.style.theme_use("clam")
        self.style.configure("A.TLabel", font="Helvetica 8 bold", background="#E6E8E8", foreground="black",
                             borderwidth=2)
        self.style.configure("B.TLabel", font="Helvetica 8 bold", background="white", foreground="black",
                             borderwidth=2)
        self.style.configure("C.TLabel", font="Helvetica 8 bold", background="white", foreground="red",
                             borderwidth=2)
        self.style.configure("A.TCombobox", font="Helvetica 8 bold", background="green", foreground="red")
        self.style.configure("A.TFrame", font="Helvetica 8 bold", foreground="black", background="yellow",
                             borderwidth=2)
        self.style.configure("B.TFrame", font="Helvetica 8 bold", foreground="black", background="#E6E8E8",
                             borderwidth=2)
        self.style.configure("C.TFrame", font="Helvetica 8 bold", foreground="black", background="orange",
                             borderwidth=2)
        self.style.configure("A.TButton", font="Helvetica 8 bold", background="grey", foreground="black", width=16)
        self.style.configure("Treeview", background="silver", foreground="black", rowheight="25",
                             fieldbackground="silver")
        self.style.map("Treeview", background=[("selected", "orange")])

        # First Selection Area
        self.lab_select_store_1 = tk.Label(self.selection_sub_frame11, text="Store\nSelection:",
                                           font="Helvetica 8 bold", background="#E6E8E8", foreground="black",
                                           borderwidth=2, height=3)
        self.lab_select_store_1.grid(row=0, column=0, padx=2, pady=2)

        # Selection and Options labels
        self.lab_store = ttk.Label(self.selection_sub_frame12, text="Store", style="A.TLabel", width=31)
        self.lab_store.grid(row=0, column=0, padx=2, pady=2)
        self.lab_store_number = ttk.Label(self.selection_sub_frame12, text="Store number", style="A.TLabel", width=13)
        self.lab_store_number.grid(row=0, column=1, padx=2, pady=2)
        self.lab_companies = ttk.Label(self.selection_sub_frame12, text="Transport company", style="A.TLabel", width=19)
        self.lab_companies.grid(row=0, column=2, padx=2, pady=2)
        self.lab_multi_id = ttk.Label(self.selection_sub_frame12, text="Multi ID", style="A.TLabel", width=8)
        self.lab_multi_id.grid(row=0, column=3, padx=2, pady=2)
        self.lab_sid = ttk.Label(self.selection_sub_frame12, text="Store in day", style="A.TLabel", width=11)
        self.lab_sid.grid(row=0, column=4, padx=2, pady=2)
        self.lab_seq = ttk.Label(self.selection_sub_frame12, text="Sequence", style="A.TLabel", width=10)
        self.lab_seq.grid(row=0, column=5, padx=2, pady=2)
        self.lab_l_type = ttk.Label(self.selection_sub_frame12, text="Loading type", style="A.TLabel", width=13)
        self.lab_l_type.grid(row=0, column=6, padx=2, pady=2)
        self.lab_t_mode = ttk.Label(self.selection_sub_frame12, text="Transport mode", style="A.TLabel", width=16)
        self.lab_t_mode.grid(row=0, column=7, padx=2, pady=2)
        self.lab_message_box = ttk.Label(self.selection_sub_frame12, text="", style="A.TLabel", width=16)
        self.lab_message_box.grid(row=0, column=9, padx=2, pady=2)

        self.lab_date = ttk.Label(self.selection_sub_frame13, text="Date", style="A.TLabel", width=13)
        self.lab_date.grid(row=0, column=0, padx=2, pady=2)
        self.lab_year = ttk.Label(self.selection_sub_frame13, text="Year", style="A.TLabel", width=6)
        self.lab_year.grid(row=0, column=1, padx=2, pady=2)
        self.lab_week = ttk.Label(self.selection_sub_frame13, text="Week", style="A.TLabel", width=6)
        self.lab_week.grid(row=0, column=2, padx=2, pady=2)
        self.lab_day = ttk.Label(self.selection_sub_frame13, text="Day", style="A.TLabel", width=6)
        self.lab_day.grid(row=0, column=3, padx=2, pady=2)
        self.lab_l_time = ttk.Label(self.selection_sub_frame13, text="Loading time", style="A.TLabel", width=13)
        self.lab_l_time.grid(row=0, column=4, padx=2, pady=2)
        self.lab_d_day = ttk.Label(self.selection_sub_frame13, text="Delivery day", style="A.TLabel", width=12)
        self.lab_d_day.grid(row=0, column=5, padx=2, pady=2)
        self.lab_d_time = ttk.Label(self.selection_sub_frame13, text="Delivery time", style="A.TLabel", width=13)
        self.lab_d_time.grid(row=0, column=6, padx=2, pady=2)
        self.lab_comment = ttk.Label(self.selection_sub_frame13, text="Comment", style="A.TLabel", width=33)
        self.lab_comment.grid(row=0, column=7, padx=2, pady=2)
        self.lab_load_id = ttk.Label(self.selection_sub_frame13, text="Load ID", style="A.TLabel", width=9)
        self.lab_load_id.grid(row=0, column=8, padx=2, pady=2)

        # Store Combobox Entry
        self.store_box = ttk.Combobox(self.selection_sub_frame12, style="TCombobox", font="Helvetica 8 bold", width=28)
        self.store_box['state'] = 'readonly'
        self.store_box['value'] = self.store_opt()
        self.store_box.grid(row=1, column=0, padx=2, pady=2)
        self.store_box.bind("<<ComboboxSelected>>", lambda event: self.store_selection(event))

        # Store Number Combobox Entry
        self.store_number_box = ttk.Combobox(self.selection_sub_frame12, style="TCombobox", font="Helvetica 8 bold",
                                             width=10)
        self.store_number_box['state'] = 'readonly'
        self.store_number_box['value'] = self.store_number_opt()
        self.store_number_box.grid(row=1, column=1, padx=2, pady=2)

        # Transport Companies Combobox Entry
        self.companies_box = ttk.Combobox(self.selection_sub_frame12, style="TCombobox", font="Helvetica 8 bold",
                                          width=16)
        self.companies_box['state'] = 'readonly'
        self.companies_box['value'] = self.companies_opt()
        self.companies_box.grid(row=1, column=2, padx=2, pady=2)

        # Multi ID Combobox Entry
        self.multi_id = ttk.Combobox(self.selection_sub_frame12, font="Helvetica 8 bold", width=5)
        self.multi_id['state'] = 'readonly'
        self.multi_id['value'] = self.multi_id_opt()
        self.multi_id.grid(row=1, column=3, padx=2, pady=2)
        self.multi_id.current(0)

        # Store in day Combobox
        self.sid = ttk.Combobox(self.selection_sub_frame12, font="Helvetica 8 bold", width=8)
        self.sid['state'] = 'readonly'
        self.sid['value'] = self.sid_opt()
        self.sid.grid(row=1, column=4, padx=2, pady=2)
        self.sid.current(0)

        # Sequence in loading Combobox
        self.sequence = ttk.Combobox(self.selection_sub_frame12, font="Helvetica 8 bold", width=7)
        self.sequence['state'] = 'readonly'
        self.sequence['value'] = self.sequence_opt()
        self.sequence.grid(row=1, column=5, padx=2, pady=2)
        self.sequence.current(0)

        # Loading types Combobox
        self.l_type = ttk.Combobox(self.selection_sub_frame12, font="Helvetica 8 bold", width=10)
        self.l_type['state'] = 'readonly'
        self.l_type['value'] = self.l_type_opt()
        self.l_type.grid(row=1, column=6, padx=2, pady=2)
        self.l_type.current(0)

        # Transport modes Combobox
        self.t_mode = ttk.Combobox(self.selection_sub_frame12, font="Helvetica 8 bold", width=13)
        self.t_mode['state'] = 'readonly'
        self.t_mode['value'] = self.t_mode_opt()
        self.t_mode.grid(row=1, column=7, padx=2, pady=2)
        self.t_mode.current(0)

        # Date choose entry
        self.cal = DateEntry(self.selection_sub_frame13, font="Helvetica 8 bold", date_pattern='MM/dd/yyyy', width=10,
                             background='grey', foreground='white', borderwidth=2, year=2020)
        self.cal.grid(row=1, column=0, padx=2, pady=2)
        self.cal.bind("<<DateEntrySelected>>", self.date_selection)

        # Year Label
        self.act_year = ttk.Label(self.selection_sub_frame13, textvariable=self.year_var, style="B.TLabel", width=6)
        self.act_year.grid(row=1, column=1, padx=2, pady=2)

        # Week Label
        self.act_week = ttk.Label(self.selection_sub_frame13, textvariable=self.week_var, style="B.TLabel", width=6)
        self.act_week.grid(row=1, column=2, padx=2, pady=2)

        # Day Label
        self.act_day = ttk.Label(self.selection_sub_frame13, textvariable=self.weekday_var, style="B.TLabel", width=6)
        self.act_day.grid(row=1, column=3, padx=2, pady=2)

        # Loading time Combobox
        self.l_time = ttk.Combobox(self.selection_sub_frame13, font="Helvetica 8 bold", width=10)
        self.l_time['state'] = 'readonly'
        self.l_time['value'] = self.l_time_opt()
        self.l_time.grid(row=1, column=4, padx=2, pady=2)
        self.l_time.current(0)

        # Delivery day Combobox
        self.d_day = ttk.Combobox(self.selection_sub_frame13, font="Helvetica 8 bold", width=9)
        self.d_day['state'] = 'readonly'
        self.d_day['value'] = self.d_day_opt()
        self.d_day.grid(row=1, column=5, padx=2, pady=2)
        self.d_day.current(0)

        # Create Delivery time entry
        self.d_time = ttk.Combobox(self.selection_sub_frame13, font="Helvetica 8 bold", width=10)
        self.d_time['state'] = 'readonly'
        self.d_time['value'] = self.d_time_opt()
        self.d_time.grid(row=1, column=6, padx=2, pady=2)
        self.d_time.current(0)

        # Comment Entry
        self.comment = ttk.Entry(self.selection_sub_frame13, font="Helvetica 8 bold", width=33,
                                 textvariable=self.comment_var)
        self.comment.grid(row=1, column=7, padx=2, pady=2)
        self.comment_var.trace("w", lambda*args: self.comment_character_limit())

        # Loading ID Entry
        self.loading_id_box = ttk.Entry(self.selection_sub_frame13, textvariable=self.create_load_id_var,
                                        font="Helvetica 8 bold", width=18)
        self.loading_id_box.grid(row=1, column=8, padx=2, pady=2)

        # Loading ID Button
        self.load_id_button = ttk.Button(self.selection_sub_frame13, text="Get Loading ID", style="A.TButton",
                                         command=lambda: self.load_id())
        self.load_id_button.grid(row=1, column=9, rowspan=1, padx=2, pady=0, ipady=0)

        # Submit loading Button
        self.submit_button = ttk.Button(self.selection_sub_frame13, text="Submit Loading", style="A.TButton",
                                        command=lambda: self.db_submit())
        self.submit_button.grid(row=1, column=10, rowspan=1, padx=2, pady=0, ipady=0)

        # Year Label
        self.empty_field = ttk.Label(self.selection_sub_frame13, text="", style="A.TLabel", width=3)
        self.empty_field.grid(row=1, column=11, padx=2, pady=2)

        self.update_button = ttk.Button(self.selection_sub_frame13, text="Update Loading", style="A.TButton",
                                        command=lambda: self.update_record())
        self.update_button.grid(row=1, column=12, padx=2, pady=2)

        # Clear Fields Button
        self.clear_fields_button = ttk.Button(self.selection_sub_frame12, text="Clear Fields", style="A.TButton",
                                              command=lambda: self.clear_fields())
        self.clear_fields_button.grid(row=1, column=8, rowspan=1, padx=2, pady=0, ipady=0)

        # Message box
        self.message_field = ttk.Label(self.selection_sub_frame12, textvariable=self.message_var,
                                       style="C.TLabel", width=40)
        self.message_field.grid(row=1, column=9, padx=2, pady=2)

        # Y Scrollbar for Tree
        self.tree_scroll = ttk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side="right", fill="y", padx=2, pady=5, anchor="nw")

        # Tree
        self.tp_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
        self.tp_tree.tag_configure("odd_row", background="white")
        self.tp_tree.tag_configure("even_row", background="#E3F7F7")
        self.tp_tree.bind("<Double-1>", self.clicker)

        # Configure Scrollbar
        self.tree_scroll.config(command=self.tp_tree.yview)

        # Define columns for Tree
        self.tp_tree["columns"] = ("Rowid", "Loading ID", "Year", "Week", "Date", "Day", "Multi_id", "SID", "Sequence",
                                   "Loading type", "Loading time", "Store number", "Store name", "Delivery day",
                                   "Delivery time", "Transport company", "Transport mode", "Comment")

        # Format columns of Tree
        self.tp_tree.column("#0", width=0, stretch="NO")
        self.tp_tree.column("Rowid", width=0, minwidth=0, anchor="w")
        self.tp_tree.column("Loading ID", width=110, minwidth=110, anchor="w")
        self.tp_tree.column("Year", width=40, minwidth=40, anchor="w")
        self.tp_tree.column("Week", width=40, minwidth=40, anchor="w")
        self.tp_tree.column("Date", width=70, minwidth=70, anchor="w")
        self.tp_tree.column("Day", width=35, minwidth=35, anchor="w")
        self.tp_tree.column("Multi_id", width=50, minwidth=50, anchor="w")
        self.tp_tree.column("SID", width=30, minwidth=30, anchor="w")
        self.tp_tree.column("Sequence", width=30, minwidth=30, anchor="w")
        self.tp_tree.column("Loading type", width=60, minwidth=60, anchor="w")
        self.tp_tree.column("Loading time", width=60, minwidth=60, anchor="w")
        self.tp_tree.column("Store number", width=40, minwidth=40, anchor="w")
        self.tp_tree.column("Store name", width=180, minwidth=180, anchor="w")
        self.tp_tree.column("Delivery day", width=60, minwidth=60, anchor="w")
        self.tp_tree.column("Delivery time", width=60, minwidth=60, anchor="w")
        self.tp_tree.column("Transport company", width=80, minwidth=80, anchor="w")
        self.tp_tree.column("Transport mode", width=80, minwidth=80, anchor="w")
        self.tp_tree.column("Comment", width=240, minwidth=240, anchor="w")

        # Create headings of Tree
        self.tp_tree.heading("#0", text="", anchor="w")
        self.tp_tree.heading("Rowid", text="Rowid", anchor="w")
        self.tp_tree.heading("Loading ID", text="Load ID", anchor="w")
        self.tp_tree.heading("Year", text="Year", anchor="w")
        self.tp_tree.heading("Week", text="Week", anchor="w")
        self.tp_tree.heading("Date", text="Date", anchor="w")
        self.tp_tree.heading("Day", text="Day", anchor="w")
        self.tp_tree.heading("Multi_id", text="MultiID", anchor="w")
        self.tp_tree.heading("SID", text="Sid", anchor="w")
        self.tp_tree.heading("Sequence", text="Seq", anchor="w")
        self.tp_tree.heading("Loading type", text="Ld. type", anchor="w")
        self.tp_tree.heading("Loading time", text="Ld. time", anchor="w")
        self.tp_tree.heading("Store number", text="St.No.", anchor="w")
        self.tp_tree.heading("Store name", text="Store", anchor="w")
        self.tp_tree.heading("Delivery day", text="Del. day", anchor="w")
        self.tp_tree.heading("Delivery time", text="Del. time", anchor="w")
        self.tp_tree.heading("Transport company", text="Company", anchor="w")
        self.tp_tree.heading("Transport mode", text="Tr. mode", anchor="w")
        self.tp_tree.heading("Comment", text="Comment", anchor="w")

        # Add Tree to the screen
        self.tp_tree.pack(padx=2, pady=5)

        self.qry_all_button = ttk.Button(self.query_frame2, text="Query all",
                                         command=lambda: self.db_all_query(self.tp_tree),
                                         style="A.TButton")
        self.qry_all_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(self.query_frame2, text="Delete Loading", style="A.TButton",
                                        command=lambda: self.delete_record(self.tp_tree))
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)

        self.lab_queries = ttk.Label(self.query_frame1, text="Queries:", style="A.TLabel", width=10)
        self.lab_queries.grid(row=0, column=0, padx=5, pady=5)
        self.lab_year = ttk.Label(self.query_frame1, text="Year", style="A.TLabel", width=8)
        self.lab_year.grid(row=0, column=1, padx=2, pady=5)
        self.lab_week = ttk.Label(self.query_frame1, text="Week", style="A.TLabel", width=8)
        self.lab_week.grid(row=0, column=2, padx=2, pady=5)
        self.lab_date = ttk.Label(self.query_frame1, text="Date", style="A.TLabel", width=13)
        self.lab_date.grid(row=0, column=3, padx=2, pady=5)
        self.lab_multi_id = ttk.Label(self.query_frame1, text="Multi ID", style="A.TLabel", width=8)
        self.lab_multi_id.grid(row=0, column=4, padx=2, pady=5)
        self.lab_store = ttk.Label(self.query_frame1, text="Store", style="A.TLabel", width=31)
        self.lab_store.grid(row=0, column=5, padx=2, pady=5)
        self.lab_company = ttk.Label(self.query_frame1, text="Transport company", style="A.TLabel", width=20)
        self.lab_company.grid(row=0, column=6, padx=2, pady=5)

        # Query Year Entry
        self.query_year_box = ttk.Combobox(self.query_frame1, font="Helvetica 8 bold", width=5)
        self.query_year_box['state'] = 'readonly'
        self.query_year_box['value'] = self.year_opt()
        self.query_year_box.grid(row=1, column=1, padx=5, pady=5)
        self.current_year = date.today().isocalendar()[0]
        self.query_year_box.set(self.current_year)
        self.query_year_box.bind("<<ComboboxSelected>>", lambda event: self.db_year_query(event, self.tp_tree))

        # Query Week Entry
        self.query_week_box = ttk.Combobox(self.query_frame1, font="Helvetica 8 bold", width=5)
        self.query_week_box['state'] = 'readonly'
        self.query_week_box['value'] = self.week_opt()
        self.query_week_box.grid(row=1, column=2, padx=5, pady=5)
        self.current_week_number = date.today().isocalendar()[1]
        self.query_week_box.set(self.current_week_number)
        self.query_week_box.bind("<<ComboboxSelected>>", lambda event: self.db_week_query(event, self.tp_tree))

        # Query Date entry
        self.query_cal_box = DateEntry(self.query_frame1, font="Helvetica 8 bold", date_pattern='MM/dd/yyyy', width=10,
                                       background='grey', foreground='white', borderwidth=2, year=2020)
        self.query_cal_box['state'] = 'readonly'
        self.query_cal_box.grid(row=1, column=3, padx=2, pady=5)
        self.query_cal_box.bind("<<DateEntrySelected>>", lambda event: self.db_date_query(event, self.tp_tree))

        # Query Multi ID Entry
        self.query_multi_id_box = ttk.Combobox(self.query_frame1, font="Helvetica 8 bold", width=5)
        self.query_multi_id_box['state'] = 'readonly'
        self.query_multi_id_box['value'] = self.multi_id_opt()
        self.query_multi_id_box.grid(row=1, column=4, padx=2, pady=5)
        self.query_multi_id_box.current(0)
        self.query_multi_id_box.bind("<<ComboboxSelected>>", lambda event: self.db_multi_id_query(event, self.tp_tree))

        # Query Store Entry
        self.query_store_box = ttk.Combobox(self.query_frame1, style="TCombobox", font="Helvetica 8 bold", width=28)
        self.query_store_box['state'] = 'readonly'
        self.query_store_box['value'] = self.store_opt()
        self.query_store_box.grid(row=1, column=5, padx=2, pady=5)
        self.query_store_box.bind("<<ComboboxSelected>>", lambda event: self.db_store_query(event, self.tp_tree))

        # Query Company Entry
        self.query_company_box = ttk.Combobox(self.query_frame1, style="TCombobox", font="Helvetica 8 bold", width=17)
        self.query_company_box['state'] = 'readonly'
        self.query_company_box['value'] = self.companies_opt()
        self.query_company_box.grid(row=1, column=6, padx=2, pady=5)
        self.query_company_box.bind("<<ComboboxSelected>>", lambda event: self.db_company_query(event, self.tp_tree))

        self.lab_queries2 = ttk.Label(self.query_frame3, text="Queries:", style="A.TLabel", width=10)
        self.lab_queries2.grid(row=0, column=0, padx=5, pady=5)
        self.lab_year2 = ttk.Label(self.query_frame3, text="Year", style="A.TLabel", width=8)
        self.lab_year2.grid(row=0, column=2, padx=2, pady=5)
        self.lab_week2 = ttk.Label(self.query_frame3, text="Week", style="A.TLabel", width=8)
        self.lab_week2.grid(row=0, column=4, padx=2, pady=5)
        self.lab_date2 = ttk.Label(self.query_frame3, text="Date", style="A.TLabel", width=13)
        self.lab_date2.grid(row=0, column=6, padx=2, pady=5)
        self.lab_multi_id2 = ttk.Label(self.query_frame3, text="Multi ID", style="A.TLabel", width=8)
        self.lab_multi_id2.grid(row=0, column=8, padx=2, pady=5)
        self.lab_store2 = ttk.Label(self.query_frame3, text="Store", style="A.TLabel", width=31)
        self.lab_store2.grid(row=0, column=10, padx=2, pady=5)
        self.lab_company2 = ttk.Label(self.query_frame3, text="Transport company", style="A.TLabel", width=20)
        self.lab_company2.grid(row=0, column=12, padx=2, pady=5)

        # Query Year CheckButton
        self.query_year_box2_var = tk.IntVar()
        self.query_year_box2_check = tk.Checkbutton(self.query_frame3, variable=self.query_year_box2_var,
                                                    width=1, background="grey", relief="groove")
        self.query_year_box2_check.grid(row=1, column=1, padx=5, pady=5)

        # Query Year Entry
        self.query_year_box2 = ttk.Combobox(self.query_frame3, font="Helvetica 8 bold", width=5)
        self.query_year_box2['state'] = 'readonly'
        self.query_year_box2['value'] = self.year_opt()
        self.query_year_box2.grid(row=1, column=2, padx=5, pady=5)
        self.current_year2 = date.today().isocalendar()[0]
        self.query_year_box2.set(self.current_year)
        # self.query_year_box2.bind("<<ComboboxSelected>>", lambda event: self.db_year_query(event, self.tp_tree))

        # Query Week CheckButton
        self.query_week_box2_var = tk.IntVar()
        self.query_week_box2_check = tk.Checkbutton(self.query_frame3, variable=self.query_week_box2_var,
                                                    width=1, background="grey", relief="groove")
        self.query_week_box2_check.grid(row=1, column=3, padx=5, pady=5)

        # Query Week Entry
        self.query_week_box2 = ttk.Combobox(self.query_frame3, font="Helvetica 8 bold", width=5)
        self.query_week_box2['state'] = 'readonly'
        self.query_week_box2['value'] = self.week_opt()
        self.query_week_box2.grid(row=1, column=4, padx=5, pady=5)
        self.current_week_number2 = date.today().isocalendar()[1]
        self.query_week_box2.set(self.current_week_number)
        # self.query_week_box2.bind("<<ComboboxSelected>>", lambda event: self.db_week_query(event, self.tp_tree))

        # Query Date CheckButton
        self.query_cal_box2_var = tk.IntVar()
        self.query_cal_box2_check = tk.Checkbutton(self.query_frame3, variable=self.query_cal_box2_var,
                                                   width=1, background="grey", relief="groove")
        self.query_cal_box2_check.grid(row=1, column=5, padx=5, pady=5)

        # Query Date entry
        self.query_cal_box2 = DateEntry(self.query_frame3, font="Helvetica 8 bold", date_pattern='MM/dd/yyyy', width=10,
                                        background='grey', foreground='white', borderwidth=2, year=2020)
        self.query_cal_box2.grid(row=1, column=6, padx=2, pady=5)
        # self.query_cal_box2.bind("<<DateEntrySelected>>", lambda event: self.db_date_query(event, self.tp_tree))

        # Query Multi ID CheckButton
        self.query_multi_id_box2_var = tk.IntVar()
        self.query_multi_id_check = tk.Checkbutton(self.query_frame3, variable=self.query_multi_id_box2_var,
                                                   width=1, background="grey", relief="groove")
        self.query_multi_id_check.grid(row=1, column=7, padx=5, pady=5)

        # Query Multi ID Entry
        self.query_multi_id_box2 = ttk.Combobox(self.query_frame3, font="Helvetica 8 bold", width=5)
        self.query_multi_id_box2['state'] = 'readonly'
        self.query_multi_id_box2['value'] = self.multi_id_opt()
        self.query_multi_id_box2.grid(row=1, column=8, padx=2, pady=5)
        # self.query_multi_id_box2.bind("<<ComboboxSelected>>", lambda event: self.db_multi_id_query(event,
        # self.tp_tree))

        # Query Store CheckButton
        self.query_store_box2_var = tk.IntVar()
        self.query_store_box2_check = tk.Checkbutton(self.query_frame3, variable=self.query_store_box2_var,
                                                     width=1, background="grey", relief="groove")
        self.query_store_box2_check.grid(row=1, column=9, padx=5, pady=5)

        # Query Store Entry
        self.query_store_box2 = ttk.Combobox(self.query_frame3, style="TCombobox", font="Helvetica 8 bold", width=28)
        self.query_store_box2['state'] = 'readonly'
        self.query_store_box2['value'] = self.store_opt()
        self.query_store_box2.grid(row=1, column=10, padx=2, pady=5)
        # self.query_store_box2.bind("<<ComboboxSelected>>", lambda event: self.db_store_query(event, self.tp_tree))

        # Query Company CheckButton
        self.query_company_box2_var = tk.IntVar()
        self.query_company_box2_check = tk.Checkbutton(self.query_frame3, variable=self.query_company_box2_var,
                                                       width=1, background="grey", relief="groove")
        self.query_company_box2_check.grid(row=1, column=11, padx=5, pady=5)

        # Query Company Entry
        self.query_company_box2 = ttk.Combobox(self.query_frame3, style="TCombobox", font="Helvetica 8 bold", width=17)
        self.query_company_box2['state'] = 'readonly'
        self.query_company_box2['value'] = self.companies_opt()
        self.query_company_box2.grid(row=1, column=12, padx=2, pady=5)
        # self.query_company_box2.bind("<<ComboboxSelected>>", lambda event: self.db_company_query(event, self.tp_tree))

        self.qry_multiple_button = ttk.Button(self.query_frame3, text="Query multiple",
                                              command=lambda: self.db_query_multiple(self.tp_tree),
                                              style="A.TButton")
        self.qry_multiple_button.grid(row=1, column=13, padx=5, pady=5)

        # Clear Fields Button
        self.clear_query_fields_button = ttk.Button(self.query_frame3, text="Clear Query", style="A.TButton",
                                                    command=lambda: self.clear_query_fields())
        self.clear_query_fields_button.grid(row=1, column=14, rowspan=1, padx=2, pady=0, ipady=0)


    def db_submit(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        if not self.loading_id_box.get() or not self.act_year.cget("text") or not self.act_week.cget("text") \
                or not self.cal.get() or not self.act_day.cget("text") or not self.multi_id.get() \
                or not self.sid.get() or not self.sequence.get() or not self.l_type.get() or not self.l_time.get() \
                or not self.store_number_box.get() or not self.store_box.get() or not self.d_day.get() \
                or not self.d_time.get() or not self.companies_box.get() or not self.t_mode.get():
            print("Please fill all fields out!")
            return
        self.curs.execute("INSERT INTO tpp_table VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (self.loading_id_box.get(), self.act_year.cget("text"), self.act_week.cget("text"),
                           self.cal.get(), self.act_day.cget("text"), self.multi_id.get(), self.sid.get(),
                           self.sequence.get(), self.l_type.get(), self.l_time.get(), self.store_number_box.get(),
                           self.store_box.get(), self.d_day.get(), self.d_time.get(), self.companies_box.get(),
                           self.t_mode.get(), self.comment.get()))
        self.curs.execute("SELECT * FROM tpp_table ORDER BY year ASC, date ASC, loading_time ASC, multi_id ASC, "
                          "sequence_in_loading ASC LIMIT 1")

        self.loading_id_box.delete(0, 'end')
        self.cal.delete(0, 'end')
        self.year_var.set("")
        self.week_var.set("")
        self.weekday_var.set("")
        self.store_number_box.delete(0, 'end')
        self.companies_box.delete(0, 'end')
        self.multi_id.delete(0, 'end')
        self.sid.delete(0, 'end')
        self.sequence.delete(0, 'end')
        self.l_type.delete(0, 'end')
        self.l_time.delete(0, 'end')
        self.store_box.delete(0, 'end')
        self.d_day.delete(0, 'end')
        self.d_time.delete(0, 'end')
        self.t_mode.delete(0, 'end')
        self.comment.delete(0, 'end')
        self.message_var.set("Loading submitted successfully")
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def select_record(self):
        # Clear entry boxes
        self.loading_id_box.delete(0, 'end')
        self.cal.delete(0, 'end')
        self.year_var.set("")
        self.week_var.set("")
        self.weekday_var.set("")
        self.multi_id.delete(0, 'end')
        self.sid.delete(0, 'end')
        self.sequence.delete(0, 'end')
        self.l_type.delete(0, 'end')
        self.l_time.delete(0, 'end')
        self.store_number_box.delete(0, 'end')
        self.store_box.delete(0, 'end')
        self.companies_box.delete(0, 'end')
        self.t_mode.delete(0, 'end')
        self.d_day.delete(0, 'end')
        self.d_time.delete(0, 'end')
        self.comment.delete(0, 'end')
        # Grab record number
        self.selected = self.tp_tree.focus()
        # Grab record values
        self.tree_values = self.tp_tree.item(self.selected, "values")
        # Output to entry boxes
        self.loading_id_box.insert(0, self.tree_values[1])
        self.year_var.set(self.tree_values[2])
        self.week_var.set(self.tree_values[3])
        self.weekday_var.set(self.tree_values[5])
        self.cal.insert(0, self.tree_values[4])
        self.multi_id.set(self.tree_values[6])
        self.sid.set(self.tree_values[7])
        self.sequence.set(self.tree_values[8])
        self.l_type.set(self.tree_values[9])
        self.l_time.set(self.tree_values[10])
        self.store_number_box.set(self.tree_values[11])
        self.store_box.set(self.tree_values[12])
        self.d_day.set(self.tree_values[13])
        self.d_time.set(self.tree_values[14])
        self.companies_box.set(self.tree_values[15])
        self.t_mode.set(self.tree_values[16])
        self.comment.insert(0, self.tree_values[17])
        self.message_var.set("Loading selected for update")

    def clicker(self, event):
        self.select_record()

    def update_record(self):
        # Update Selected Record
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        if not self.loading_id_box.get() or not self.act_year.cget("text") or not self.act_week.cget("text") \
                or not self.cal.get() or not self.act_day.cget("text") or not self.multi_id.get() \
                or not self.sid.get() or not self.sequence.get() or not self.l_type.get() or not self.l_time.get() \
                or not self.store_number_box.get() or not self.store_box.get() or not self.d_day.get() \
                or not self.d_time.get() or not self.companies_box.get() or not self.t_mode.get():
            print("Please fill all fields out!")
            return

        for selected_item in self.tp_tree.selection():
            self.curs.execute("UPDATE tpp_table SET loading_id=?, year=?, week=?, date=?, day=?, multi_id=?,"
                              "store_in_day=?, sequence_in_loading=?, loading_type=?, loading_time=?,"
                              "store_number=?, store_name=?, delivery_day=?, delivery_time=?,"
                              "transport_company=?, transport_mode=?, comment=?"
                              "WHERE oid=?",
                              (self.loading_id_box.get(), self.act_year.cget("text"), self.act_week.cget("text"),
                               self.cal.get(), self.act_day.cget("text"), self.multi_id.get(), self.sid.get(),
                               self.sequence.get(), self.l_type.get(), self.l_time.get(), self.store_number_box.get(),
                               self.store_box.get(), self.d_day.get(), self.d_time.get(), self.companies_box.get(),
                               self.t_mode.get(), self.comment.get(), self.tp_tree.set(selected_item, '#1'),))
            self.message_var.set("Loading updated successfully")
            self.conn.commit()
            self.curs.close()
            self.conn.close()

    def delete_record(self, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        for selected_item in tp_tree.selection():
            self.curs.execute('DELETE FROM tpp_table WHERE oid=?', (tp_tree.set(selected_item, '#1'),))
            self.conn.commit()
            self.curs.close()
            tp_tree.delete(selected_item)
            self.message_var.set("Loading deleted successfully")
        self.conn.close()

    def clear_fields(self):
        # Clear entry boxes
        self.loading_id_box.delete(0, 'end')
        self.cal.delete(0, 'end')
        self.year_var.set("")
        self.week_var.set("")
        self.weekday_var.set("")
        self.multi_id.set("")
        self.sid.set("")
        self.sequence.set("")
        self.l_type.set("")
        self.l_time.set("")
        self.store_number_box.set("")
        self.store_box.set("")
        self.companies_box.set("")
        self.t_mode.set("")
        self.d_day.set("")
        self.d_time.set("")
        self.comment.delete(0, 'end')
        self.message_var.set("")

    # Store selection function
    def store_selection(self, event):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_store = event.widget.get()
        # Set Store Number combobox according to the Store name
        set_store_number_box = self.curs.execute('SELECT store_number FROM stores_list WHERE store_name=?', [sel_store])
        row_store_number = set_store_number_box.fetchone()[0]
        self.store_number_box.set(row_store_number)
        # Set Transport company combobox to the Store's default company
        set_companies_box = self.curs.execute('SELECT default_transport_company FROM stores_list WHERE store_name=?',
                                              [sel_store])
        row_companies = set_companies_box.fetchone()[0]
        self.companies_box.set(row_companies)
        # Set Multi ID number combobox to the default Multi ID number of the Store
        set_multi_id_box = self.curs.execute('SELECT default_multi_id FROM stores_list WHERE store_name=?', [sel_store])
        row_multi_id = set_multi_id_box.fetchone()[0]
        self.multi_id.set(row_multi_id)
        # Set Loading type combobox to the default Loading type of the Store
        set_l_type = self.curs.execute('SELECT default_loading_type FROM stores_list WHERE store_name=?', [sel_store])
        row_l_type = set_l_type.fetchone()[0]
        self.l_type.set(row_l_type)
        # Set Transport mode combobox to the default Transport mode of the Store
        set_t_mode = self.curs.execute('SELECT default_transport_mode FROM stores_list WHERE store_name=?', [sel_store])
        row_t_mode = set_t_mode.fetchone()[0]
        self.t_mode.set(row_t_mode)
        # Set Sequence combobox to the default Sequence of the Store
        set_sequence = self.curs.execute('SELECT default_sequence FROM stores_list WHERE store_name=?', [sel_store])
        row_sequence = set_sequence.fetchone()[0]
        self.sequence.set(row_sequence)
        # Set Loading Time combobox to the default Loading Time of the Store
        set_l_time = self.curs.execute('SELECT default_loading_time FROM stores_list WHERE store_name=?', [sel_store])
        row_l_time = set_l_time.fetchone()[0]
        self.l_time.set(row_l_time)
        # Set Delivery Day combobox to the default Delivery Day of the Store
        set_d_day = self.curs.execute('SELECT default_delivery_day FROM stores_list WHERE store_name=?', [sel_store])
        row_d_day = set_d_day.fetchone()[0]
        self.d_day.set(row_d_day)
        # Set Delivery Time combobox to the default Delivery Time of the Store
        set_d_time = self.curs.execute('SELECT default_delivery_time FROM stores_list WHERE store_name=?', [sel_store])
        row_d_time = set_d_time.fetchone()[0]
        self.d_time.set(row_d_time)
        # Set SID combobox to the default SID of the Store
        set_sid = self.curs.execute('SELECT default_SID FROM stores_list WHERE store_name=?', [sel_store])
        row_sid = set_sid.fetchone()[0]
        self.sid.set(row_sid)
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def comment_character_limit(self):
        if len(self.comment_var.get()) > 0:
            self.comment_var.set(self.comment_var.get()[:30])

    def comment_character_limit2(self):
        if len(self.comment_var2.get()) > 0:
            self.comment_var2.set(self.comment_var2.get()[:30])

    def load_id(self):
        self.create_load_id = str(self.multi_id.get()) + str(self.store_number_box.get()) + str(self.sid.get()) + \
                              str(self.sequence.get()) + str(self.cal.get())[0:2] + str(self.cal.get())[3:5] + \
                              str(self.cal.get())[6:10]
        self.create_load_id_var.set(self.create_load_id)

    # Multi ID Combobox function
    def multi_id_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT multi_id From multi_ids')
        data_multi_id = []
        for row in self.curs.fetchall():
            data_multi_id.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_multi_id

    # Sequence in loading combobox function
    def sequence_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT sequence FROM sequence_in_loading')
        data_seq = []
        for row in self.curs.fetchall():
            data_seq.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_seq

    # Loading type combobox function
    def l_type_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT loading_type FROM loading_types')
        data_load_type = []
        for row in self.curs.fetchall():
            data_load_type.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_load_type

    # Store in day combobox function
    def sid_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT store_in_day FROM stores_in_day')
        data_s_id = []
        for row in self.curs.fetchall():
            data_s_id.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_s_id

    # Day combobox function
    def l_day_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT day FROM days')
        data_day = []
        for row in self.curs.fetchall():
            data_day.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_day

    def date_selection(self, event):
        sel_date = event.widget.get()
        sd = parse(sel_date)
        week = datetime.date(sd).isocalendar()
        self.week_var.set(week[1])
        year = datetime.date(sd).isocalendar()
        self.year_var.set(year[0])
        day = datetime.date(sd).isocalendar()
        day_number = day[2]
        if day_number == 1:
            self.weekday_var.set("Mon")
        elif day_number == 2:
            self.weekday_var.set("Tue")
        elif day_number == 3:
            self.weekday_var.set("Wed")
        elif day_number == 4:
            self.weekday_var.set("Thu")
        elif day_number == 5:
            self.weekday_var.set("Fri")
        elif day_number == 6:
            self.weekday_var.set("Sat")
        elif day_number == 7:
            self.weekday_var.set("Sun")

    # Week combobox function
    def l_week_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT week FROM weeks')
        data_week = []
        for row in self.curs.fetchall():
            data_week.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_week

    # Year combobox function
    def l_year_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT year FROM years')
        data_year = []
        for row in self.curs.fetchall():
            data_year.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_year

    # Loading time combobox function
    def l_time_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT time_value FROM time_values')
        data_load_time = []
        for row in self.curs.fetchall():
            data_load_time.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_load_time

    # Delivery day combobox function
    def d_day_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT d_day FROM delivery_day')
        data_d_day = []
        for row in self.curs.fetchall():
            data_d_day.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_d_day

    # Delivery time combobox function
    def d_time_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT time_value FROM time_values')
        data_deliver_time = []
        for row in self.curs.fetchall():
            data_deliver_time.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_deliver_time

    # Loading mode combobox function
    def t_mode_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT transport_mode FROM transport_modes')
        data_trans_mode = []
        for row in self.curs.fetchall():
            data_trans_mode.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_trans_mode

    def year_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT year FROM years')
        data_year = []
        for row in self.curs.fetchall():
            data_year.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_year

    def week_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT week FROM weeks')
        data_week = []
        for row in self.curs.fetchall():
            data_week.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_week

    # Store combobox function
    def store_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT store_name From stores_list')
        datastore = []
        for row in self.curs.fetchall():
            datastore.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return datastore

    # Store number combobox function
    def store_number_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT store_number From stores_list')
        data_store_number = []
        for row in self.curs.fetchall():
            data_store_number.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return data_store_number

    # Transport companies combobox function
    def companies_opt(self):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute('SELECT company_name FROM transport_companies')
        companies = []
        for row in self.curs.fetchall():
            companies.append(row[0])
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        return companies

    def db_all_query(self, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        self.curs.execute("SELECT * FROM tpp_table ORDER BY year ASC, date ASC, loading_time ASC, multi_id ASC, "
                          "sequence_in_loading ASC")
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_week_query(self, event, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_week = event.widget.get()
        self.curs.execute("SELECT * FROM tpp_table WHERE week=? ORDER BY year ASC, date ASC, loading_time ASC, "
                          "multi_id ASC, sequence_in_loading ASC", [sel_week])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_year_query(self, event, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_year = event.widget.get()
        self.curs.execute("SELECT * FROM tpp_table WHERE year=? ORDER BY year ASC, date ASC, loading_time ASC, "
                          "multi_id ASC, sequence_in_loading ASC", [sel_year])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_date_query(self, event, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_date = event.widget.get()
        self.curs.execute("SELECT * FROM tpp_table WHERE date=? ORDER BY loading_time ASC, multi_id ASC, "
                          "sequence_in_loading ASC", [sel_date])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_multi_id_query(self, event, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_multi_id = event.widget.get()
        self.curs.execute("SELECT * FROM tpp_table WHERE multi_id=? ORDER BY year ASC, date ASC, loading_time ASC, "
                          "sequence_in_loading ASC", [sel_multi_id])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_store_query(self, event, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_store_query = event.widget.get()
        self.curs.execute("SELECT * FROM tpp_table WHERE store_name=? ORDER BY year ASC, date ASC, loading_time ASC, "
                          "multi_id ASC, sequence_in_loading ASC", [sel_store_query])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_company_query(self, event, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        sel_company = event.widget.get()
        self.curs.execute("SELECT * FROM tpp_table WHERE transport_company=? ORDER BY year ASC, date ASC, "
                          "loading_time ASC, multi_id ASC, sequence_in_loading ASC", [sel_company])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def db_query_multiple(self, tp_tree):
        self.conn = sqlite3.connect("files/db_transport_planner.db")
        self.curs = self.conn.cursor()
        if self.query_year_box2_var.get() == 1:
            self.sel_year_multi_query = self.query_year_box2.get()
        elif self.query_year_box2_var.get() == 0:
            self.sel_year_multi_query = "%"

        if self.query_week_box2_var.get() == 1:
            self.sel_week_multi_query = self.query_week_box2.get()
        elif self.query_week_box2_var.get() == 0:
            self.sel_week_multi_query = "%"

        if self.query_cal_box2_var.get() == 1:
            self.sel_cal_multi_query = self.query_cal_box2.get()
        elif self.query_cal_box2_var.get() == 0:
            self.sel_cal_multi_query = "%"

        if self.query_multi_id_box2_var.get() == 1:
            self.sel_multi_id_multi_query = self.query_multi_id_box2.get()
        elif self.query_multi_id_box2_var.get() == 0:
            self.sel_multi_id_multi_query = "%"

        if self.query_store_box2_var.get() == 1:
            self.sel_store_multi_query = self.query_store_box2.get()
        elif self.query_store_box2_var.get() == 0:
            self.sel_store_multi_query = "%"

        if self.query_company_box2_var.get() == 1:
            self.sel_company_multi_query = self.query_company_box2.get()
            print(self.sel_company_multi_query)
        elif self.query_company_box2_var.get() == 0:
            self.sel_company_multi_query = "%"
            print(self.sel_company_multi_query)

        self.curs.execute("SELECT * FROM tpp_table WHERE "
                          "year IS (?) AND "
                          "week IS (?) AND "
                          "date IS (?) AND "
                          "multi_id IS (?) AND "
                          "store_name IS (?) AND "
                          "transport_company = ? "
                          "ORDER BY year ASC, date ASC, "
                          "loading_time ASC, multi_id ASC, sequence_in_loading ASC",
                          [self.sel_year_multi_query, self.sel_week_multi_query, self.sel_cal_multi_query,
                           self.sel_multi_id_multi_query, self.sel_store_multi_query, self.sel_company_multi_query])
        self.data_s = self.curs.fetchall()
        self.tp_tree.delete(*tp_tree.get_children())
        row_number = 1
        for data in self.data_s:
            if row_number % 2 == 0:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="even_row")
            else:
                self.tp_tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5],
                                                       data[6], data[7], data[8], data[9], data[10], data[11],
                                                       data[12], data[13], data[14], data[15], data[16], data[17]),
                                    tags="odd_row")
            row_number += 1
        self.conn.commit()
        self.curs.close()
        self.conn.close()

    def clear_query_fields(self):
        # Clear query boxes
        self.query_year_box2.set("")
        self.query_week_box2.set("")
        self.query_cal_box2.delete(0, 'end')
        self.query_multi_id_box2.set("")
        self.query_store_box2.set("")
        self.query_company_box2.set("")


def main():
    root = tk.Tk()
    # width = root.winfo_screenwidth()
    # height = root.winfo_screenheight()
    # root.geometry(f'{width}x{height}')
    root.geometry("1303x590")
    root.resizable(False, False)
    root.title("Transport Planner")
    MainApp(root, sel_company_multi_query=None)
    root.mainloop()


if __name__ == "__main__":
    main()
