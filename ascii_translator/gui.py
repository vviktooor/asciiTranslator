"""Tkinter window in WR colours with an English/Polish switch. Author: WR"""

import customtkinter as ctk

from . import convert, i18n
from .theme import ERROR, INK, INK_2, LINE, MONO, MUTED, PAPER, SANS, SIGNAL, SIGNAL_HOVER, SLATE


class App(ctk.CTk):
    def __init__(self, lang: str):
        super().__init__(fg_color=INK)
        ctk.set_appearance_mode("dark")
        self.geometry("760x560")
        self.minsize(560, 460)
        self.lang = lang
        self.text = i18n.load(lang)
        self._build()

    def _build(self):
        for child in self.winfo_children():
            child.destroy()
        t = self.text
        self.title(f"WR · {t['title']}")

        head = ctk.CTkFrame(self, fg_color=INK, corner_radius=0)
        head.pack(fill="x", padx=24, pady=(20, 8))
        ctk.CTkLabel(head, text="WR", text_color=SIGNAL, font=(SANS, 22, "bold")).pack(side="left")
        ctk.CTkLabel(head, text=f"  {t['title']}", text_color=PAPER, font=(SANS, 18, "bold")).pack(side="left")
        switch = ctk.CTkSegmentedButton(
            head,
            values=["EN", "PL"],
            command=self._set_lang,
            font=(SANS, 12, "bold"),
            fg_color=INK_2,
            selected_color=SIGNAL,
            selected_hover_color=SIGNAL_HOVER,
            unselected_color=INK_2,
            unselected_hover_color=LINE,
            text_color=PAPER,
        )
        switch.set(self.lang.upper())
        switch.pack(side="right")

        tabs = ctk.CTkTabview(
            self,
            fg_color=INK_2,
            corner_radius=12,
            border_width=1,
            border_color=LINE,
            segmented_button_fg_color=INK,
            segmented_button_selected_color=SIGNAL,
            segmented_button_selected_hover_color=SIGNAL_HOVER,
            segmented_button_unselected_color=INK,
            segmented_button_unselected_hover_color=LINE,
            text_color=PAPER,
        )
        tabs.pack(fill="both", expand=True, padx=24, pady=(0, 24))
        self.tabs = tabs
        self._pane(tabs.add(t["tab_to_ascii"]), t["hint_to_ascii"], convert.text_to_ascii)
        self._pane(tabs.add(t["tab_to_text"]), t["hint_to_text"], convert.ascii_to_text)

    def _pane(self, tab, hint, func):
        t = self.text
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure((1, 4), weight=1)
        box = dict(fg_color=INK, border_color=LINE, border_width=1, corner_radius=8, text_color=PAPER, font=(MONO, 13))

        ctk.CTkLabel(tab, text=t["input"], text_color=MUTED, font=(SANS, 12)).grid(row=0, column=0, sticky="w")
        source = ctk.CTkTextbox(tab, **box)
        source.grid(row=1, column=0, sticky="nsew")
        ctk.CTkLabel(tab, text=hint, text_color=SLATE, font=(SANS, 11)).grid(row=2, column=0, sticky="w", pady=(4, 0))

        bar = ctk.CTkFrame(tab, fg_color="transparent")
        bar.grid(row=3, column=0, sticky="ew", pady=10)
        status = ctk.CTkLabel(bar, text="", text_color=ERROR, font=(SANS, 12))
        result = ctk.CTkTextbox(tab, **box)

        def run():
            result.delete("1.0", "end")
            status.configure(text="")
            try:
                result.insert("1.0", func(source.get("1.0", "end-1c")))
            except ValueError as error:
                status.configure(text=t["error_code"].format(token=error))

        def clear():
            source.delete("1.0", "end")
            result.delete("1.0", "end")
            status.configure(text="")

        ctk.CTkButton(
            bar,
            text=t["convert"],
            command=run,
            fg_color=SIGNAL,
            hover_color=SIGNAL_HOVER,
            text_color=INK,
            font=(SANS, 13, "bold"),
            corner_radius=8,
            width=140,
        ).pack(side="left")
        ctk.CTkButton(
            bar,
            text=t["clear"],
            command=clear,
            fg_color="transparent",
            hover_color=LINE,
            border_width=1,
            border_color=LINE,
            text_color=PAPER,
            font=(SANS, 13),
            corner_radius=8,
            width=100,
        ).pack(side="left", padx=8)
        status.pack(side="left", padx=8)

        ctk.CTkLabel(tab, text=t["output"], text_color=MUTED, font=(SANS, 12)).grid(row=4, column=0, sticky="nw")
        result.grid(row=4, column=0, sticky="nsew", pady=(22, 0))
        tab.source, tab.result, tab.run = source, result, run

    def _set_lang(self, value: str):
        self.lang = value.lower()
        self.text = i18n.load(self.lang)
        self._build()


def main():
    App(i18n.default_language()).mainloop()
