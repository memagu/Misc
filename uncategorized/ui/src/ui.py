from __future__ import annotations
import datetime
import tkinter as tk
import tkinter.ttk as ttk
from typing import Optional

import tkcalendar
from PIL import Image, ImageTk

import calendanielsson
from constants import PATH_ICONS


class ActivityFrame(ttk.Frame):
    def __init__(self, master: App | ttk.Frame, activity: calendanielsson.Activity):
        super().__init__(master)

        date_entry = tkcalendar.DateEntry(
            self,
            date_pattern="yyyy-mm-dd",
            yearint=activity.start.year,
            monthint=activity.start.month,
            dayint=activity.start.day,
            width=10
        )
        date_entry.grid(row=0, column=1)

        self.start_hour = tk.StringVar(value=f"{activity.start:%H}")
        start_hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, format="%02.0f", width=3,
                                         textvariable=self.start_hour)
        start_hour_spinbox.grid(row=0, column=2)

        start_separator = ttk.Label(self, text=':')
        start_separator.grid(row=0, column=3)

        self.start_minute = tk.StringVar(value=f"{activity.start:%M}")
        start_minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, format="%02.0f", width=3,
                                           textvariable=self.start_minute)
        start_minute_spinbox.grid(row=0, column=4)

        start_separator = ttk.Label(self, text='-->')
        start_separator.grid(row=0, column=5)

        self.end_hour = tk.StringVar(value=f"{activity.end:%H}")
        end_hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, format="%02.0f", width=3,
                                       textvariable=self.end_hour)
        end_hour_spinbox.grid(row=0, column=6)

        end_separator = ttk.Label(self, text=':')
        end_separator.grid(row=0, column=7)

        self.end_minute = tk.StringVar(value=f"{activity.end:%M}")
        end_minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, format="%02.0f", width=3,
                                         textvariable=self.end_minute)
        end_minute_spinbox.grid(row=0, column=8)

        note_entry = ttk.Entry(self)
        note_entry.insert(0, activity.note)
        note_entry.grid(row=0, column=9)


class PageFrame(ttk.Frame):
    def __init__(self, master: App | ttk.Frame, page: calendanielsson.Page):
        super().__init__(master)

        self.date = ttk.Label(self, text=f"{page.date:%Y-%m-%d}", anchor="w")
        self.date.grid(row=0, column=0, sticky="ew")

        for i, activity in enumerate(page.activities):
            row = i + 1

            btn_delete = ttk.Button(self, image=master.icons["trash_can"],
                                    command=lambda: (page.delete_activity(i), master.show_page()))
            btn_delete.grid(row=row, column=0)

            activity_frame = ActivityFrame(self, activity)
            activity_frame.grid(row=row, column=1)


class CreateActivityFrame(ttk.Frame):
    def __init__(self, master: App | ttk.Frame):
        super().__init__(master)

        self.submit_button = ttk.Button(self, image=master.icons["check_mark"], command=lambda: (
        master.calendar.create_activity(*self.fetch_info()), master.show_page()))
        self.submit_button.grid(row=0, column=1)

        self.date_entry = tkcalendar.DateEntry(self, date_pattern="yyyy-mm-dd", width=10)
        self.date_entry.grid(row=0, column=2)

        self.start_hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, format="%02.0f", width=3)
        self.start_hour_spinbox.grid(row=0, column=3)

        self.start_separator = ttk.Label(self, text=':')
        self.start_separator.grid(row=0, column=4)

        self.start_minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, format="%02.0f", width=3)
        self.start_minute_spinbox.grid(row=0, column=5)

        self.start_separator = ttk.Label(self, text='-->')
        self.start_separator.grid(row=0, column=6)

        self.end_hour_spinbox = ttk.Spinbox(self, from_=0, to=23, wrap=True, format="%02.0f", width=3)
        self.end_hour_spinbox.grid(row=0, column=7)

        self.end_separator = ttk.Label(self, text=':')
        self.end_separator.grid(row=0, column=8)

        self.end_minute_spinbox = ttk.Spinbox(self, from_=0, to=59, wrap=True, format="%02.0f", width=3)
        self.end_minute_spinbox.grid(row=0, column=9)

        self.note_entry = ttk.Entry(self)
        self.note_entry.grid(row=0, column=10)

    def fetch_info(self) -> tuple[datetime.datetime, datetime.datetime, datetime.datetime, str]:
        date = datetime.datetime.combine(self.date_entry.get_date(), datetime.time())
        start = datetime.datetime.combine(date, datetime.datetime.strptime(
            self.start_hour_spinbox.get() + self.start_minute_spinbox.get(), "%H%M").time())
        end = datetime.datetime.combine(date, datetime.datetime.strptime(
            self.end_hour_spinbox.get() + self.end_minute_spinbox.get(), "%H%M").time())
        note = self.note_entry.get()

        return date, start, end, note


class NavbarFrame(ttk.Frame):
    def __init__(self, master: App | ttk.Frame):
        super().__init__(master)

        btn_previous = ttk.Button(self, image=master.icons["arrow_left"], command=master.previous_page)
        btn_previous.grid(row=0, column=0)

        btn_next = ttk.Button(self, image=master.icons["arrow_right"], command=master.next_page)
        btn_next.grid(row=0, column=1)

        btn_add = ttk.Button(self, image=master.icons["plus"], command=master.create_activity)
        btn_add.grid(row=0, column=2)

        btn_delete = ttk.Button(self, image=master.icons["trash_can"], command=master.delete_page)
        btn_delete.grid(row=0, column=3)

        btn_show_all = ttk.Button(self, image=master.icons["calendar"])
        btn_show_all.grid(row=0, column=4)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kalendanielsson")
        self.geometry("800x450")

        self.grid_columnconfigure(0, weight=1)  # as did this

        self.icons = self.load_icons((32, 32))
        self.calendar = calendanielsson.get_test_calendar()

        self.navbar = NavbarFrame(self)
        self.navbar.grid(row=0, column=0, sticky="ew")

        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=0, sticky="ew")

        self.page_frame = None
        self.create_activity_frame = None

        self.show_page()


    def load_icons(self, icon_size: Optional[tuple[int, int]] = None) -> dict[str, tk.PhotoImage]:
        icons = {}

        for icon_path in PATH_ICONS.iterdir():
            img = Image.open(icon_path)

            if icon_size is not None:
                img = img.resize(icon_size)

            icons[icon_path.stem] = ImageTk.PhotoImage(img)

        return icons

    def show_page(self) -> None:
        if self.create_activity_frame is not None:
            self.create_activity_frame.grid_forget()

        if self.page_frame is not None:
            self.page_frame.grid_forget()

        if not self.calendar.pages:
            return

        self.page_frame = PageFrame(self, self.calendar.pages[self.calendar.page_index])
        self.page_frame.grid(row=2, column=0, sticky="ew")

    def next_page(self) -> None:
        self.calendar.browse(1)
        self.show_page()

    def previous_page(self) -> None:
        self.calendar.browse(-1)
        self.show_page()

    def delete_page(self):
        self.calendar.delete_current_page()
        self.show_page()

    def create_activity(self):
        if self.page_frame is not None:
            self.page_frame.grid_forget()

        self.create_activity_frame = CreateActivityFrame(self)
        self.create_activity_frame.grid(row=2, column=0, sticky="ew")
