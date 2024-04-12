from __future__ import annotations
import datetime
import tkinter as tk
from typing import Optional

from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs.dialogs import Messagebox

import calendanielsson
from constants import PATH_APP_ICON, PATH_ICONS


class ScrollableTreeview(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=ttk.RIGHT, fill=ttk.Y)

class ActivityFrame(ttk.Frame):
    def __init__(self, master: tk.Widget, activities: list[calendanielsson.Activity]):
        super().__init__(master)
        self.activities = activities

        self.activity_table = ScrollableTreeview(self, columns=("date", "start", "end", "note"), show="headings",
                                                 selectmode=ttk.BROWSE)

        self.activity_table.heading("date", text="Date")
        self.activity_table.column("date", anchor=ttk.CENTER, width=100, stretch=ttk.NO)

        self.activity_table.heading("start", text="Start time")
        self.activity_table.column("start", anchor=ttk.CENTER, width=100, stretch=ttk.NO)

        self.activity_table.heading("end", text="End time")
        self.activity_table.column("end", anchor=ttk.CENTER, width=100, stretch=ttk.NO)

        self.activity_table.heading("note", text="Note")
        self.activity_table.column("note", anchor=ttk.CENTER)

        for activity in self.activities:
            self.activity_table.insert('', ttk.END, values=(
                activity.start.strftime("%Y-%m-%d"),
                activity.start.strftime("%H:%M"),
                activity.end.strftime("%H:%M"),
                activity.note
            ))

        self.activity_table.bind("<<TreeviewSelect>>", lambda _: self.on_activity_selection())

        self.activity_table.pack(fill=ttk.BOTH, expand=ttk.YES)

    def on_activity_selection(self):
        selected_activity = self.activities[self.activity_table.index(self.activity_table.selection())]
        self.winfo_toplevel().activity_editor.set_values_from_activity(selected_activity)
        self.winfo_toplevel().selected_activity = selected_activity


class ActivityEditorFrame(ttk.Frame):
    def __init__(self, master: tk.Widget):
        super().__init__(master)

        self.edit_button = ttk.Button(self, image=self.winfo_toplevel().icons["trash_can"], command=self.winfo_toplevel().delete_current_activity)
        self.edit_button.pack(side=ttk.LEFT)

        self.edit_button = ttk.Button(self, image=self.winfo_toplevel().icons["edit"],
                                      command=lambda: self.winfo_toplevel().edit_current_activity(*self.fetch_values()))
        self.edit_button.pack(side=ttk.LEFT)

        self.date_entry = ttk.DateEntry(self, dateformat="%Y-%m-%d", width=10)
        self.date_entry.pack(side=ttk.LEFT)

        self.start_hour = ttk.IntVar()
        self.start_hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, format="%02.0f", width=2,
                                              textvariable=self.start_hour)
        self.start_hour_spinbox.pack(side=ttk.LEFT)

        self.start_separator = ttk.Label(self, text=':')
        self.start_separator.pack(side=ttk.LEFT)

        self.start_minute = ttk.IntVar()
        self.start_minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, format="%02.0f", width=2,
                                                textvariable=self.start_minute)
        self.start_minute_spinbox.pack(side=ttk.LEFT)

        self.start_separator = ttk.Label(self, text='-->')
        self.start_separator.pack(side=ttk.LEFT)

        self.end_hour = ttk.IntVar()
        self.end_hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, format="%02.0f", width=2,
                                            textvariable=self.end_hour)
        self.end_hour_spinbox.pack(side=ttk.LEFT)

        self.end_separator = ttk.Label(self, text=':')
        self.end_separator.pack(side=ttk.LEFT)

        self.end_minute = ttk.IntVar()
        self.end_minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, format="%02.0f", width=2,
                                              textvariable=self.end_minute)
        self.end_minute_spinbox.pack(side=ttk.LEFT)

        self.note = ttk.StringVar()
        self.note_entry = ttk.Entry(self, textvariable=self.note)
        self.note_entry.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.TRUE)

        self.add_button = ttk.Button(self, image=self.winfo_toplevel().icons["plus"],
                                     command=lambda: self.winfo_toplevel().create_activity(*self.fetch_values()))
        self.add_button.pack(side=ttk.RIGHT)

    def set_values_from_activity(self, activity: calendanielsson.Activity):
        self.date_entry.entry.delete(0, ttk.END)
        self.date_entry.entry.insert(0, activity.start.strftime("%Y-%m-%d"))
        self.start_hour.set(activity.start.hour)
        self.start_minute.set(activity.start.minute)
        self.end_hour.set(activity.end.hour)
        self.end_minute.set(activity.end.minute)
        self.note.set(activity.note)

    def fetch_values(self):
        date = datetime.datetime.strptime(self.date_entry.entry.get(), "%Y-%m-%d")
        start = datetime.datetime.combine(
            date,
            datetime.time(self.start_hour.get(), self.start_minute.get())
        )
        end = datetime.datetime.combine(
            date,
            datetime.time(self.end_hour.get(), self.end_minute.get())
        )
        note = self.note.get()

        return date, start, end, note


class NavbarFrame(ttk.Frame):
    def __init__(self, master: tk.Widget):
        super().__init__(master)

        btn_previous = ttk.Button(self, image=self.winfo_toplevel().icons["arrow_left"], command=self.winfo_toplevel().previous_page)
        btn_previous.pack(side=ttk.LEFT)

        btn_next = ttk.Button(self, image=self.winfo_toplevel().icons["arrow_right"], command=self.winfo_toplevel().next_page)
        btn_next.pack(side=ttk.LEFT)

        btn_show_all = ttk.Button(self, image=self.winfo_toplevel().icons["calendar"], command=self.winfo_toplevel().view_all_pages)
        btn_show_all.pack(side=ttk.LEFT)

        btn_delete = ttk.Button(self, image=self.winfo_toplevel().icons["trash_can"], command=self.winfo_toplevel().delete_page)
        btn_delete.pack(side=ttk.LEFT)


class App(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Calendanielsson")
        self.iconbitmap(PATH_APP_ICON)
        self.geometry("800x450")

        self.icons = self.load_icons((32, 32))
        self.calendar = calendanielsson.get_test_calendar(20)

        self.navbar = NavbarFrame(self)
        self.navbar.pack(fill=ttk.X)

        self.separator = ttk.Separator(self)
        self.separator.pack(fill=ttk.X)

        self.page_notebook = ttk.Notebook(self)
        self.page_notebook.bind("<<NotebookTabChanged>>",
                                lambda _: self.set_page_index(self.page_notebook.index(ttk.CURRENT)))
        self.update_notebook()
        self.page_notebook.pack(fill=ttk.BOTH, expand=ttk.TRUE)

        self.selected_activity = None
        self.activity_editor = ActivityEditorFrame(self)
        self.activity_editor.pack(fill=ttk.X)

    def load_icons(self, icon_size: Optional[tuple[int, int]] = None) -> dict[str, tk.PhotoImage]:
        icons = {}

        for icon_path in PATH_ICONS.iterdir():
            img = Image.open(icon_path)

            if icon_size is not None:
                img = img.resize(icon_size)

            icons[icon_path.stem] = ImageTk.PhotoImage(img)

        return icons

    def update_notebook(self):
        for tab in self.page_notebook.winfo_children():
            tab.destroy()

        for page in self.calendar.pages:
            self.page_notebook.add(ActivityFrame(self.page_notebook, page.activities), text=page.date.strftime("%Y-%m-%d"))

        self.page_notebook.add(ActivityFrame(self.page_notebook, [activity for page in self.calendar.pages for activity in page.activities]), text="All activities")

        self.page_notebook.select(self.calendar.page_index)

    def previous_page(self):
        self.calendar.browse(-1)
        self.page_notebook.select(self.calendar.page_index)

    def next_page(self):
        self.calendar.browse(1)
        self.page_notebook.select(self.calendar.page_index)

    def delete_page(self):
        if not self.calendar.pages:
            return

        self.page_notebook.forget(self.calendar.page_index)
        self.calendar.delete_current_page()
        self.page_notebook.select(self.calendar.page_index)

        self.update_notebook()

    def view_all_pages(self) -> None:
        self.page_notebook.select(len(self.calendar.pages))

    def set_selected_activity(self, activity: calendanielsson.Activity) -> None:
        self.selected_activity = activity

    def set_page_index(self, index):
        if 0 <= index < len(self.calendar.pages):
            self.calendar.page_index = index

    def create_activity(self, date: datetime.datetime, start: datetime.datetime, end: datetime.datetime,
                        note: str) -> None:

        if end < start:
            return

        self.calendar.create_activity(date, start, end, note)
        self.page_notebook.select(self.calendar.page_index)

        self.update_notebook()

    def edit_current_activity(self, date: datetime.datetime, start: datetime.datetime,
                      end: datetime.datetime, note: str) -> None:
        if self.selected_activity is None:
            return

        if end < start:
            return

        self.calendar.delete_activity(self.selected_activity)
        self.create_activity(date, start, end, note)

        self.set_selected_activity(None)
        self.update_notebook()

    def delete_current_activity(self):
        if self.selected_activity is None:
            return

        self.calendar.delete_activity(self.selected_activity)

        self.set_selected_activity(None)
        self.update_notebook()