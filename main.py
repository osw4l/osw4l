from datetime import datetime

import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"


def main():
    t = gifos.Terminal(750, 380, 15, 15, FONT_FILE_BITMAP, 15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y")

    # BIOS boot
    t.gen_text("GIF_OS Modular BIOS v2.0.4", 1)
    t.gen_text(
        f"Copyright (C) {year_now}, \x1b[32mosw4l Systems Inc.\x1b[0m", 2
    )
    t.gen_text("\x1b[94mGitHub Profile Terminal, Rev 2004\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 500Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Memory Test: {i}", 7, count=2, contin=True)
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    # OS Logo
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)
    t.set_font(FONT_FILE_LOGO, 66)
    os_logo_text = "GIF OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    # Login
    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mGIF OS v2.0.4 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("osw4l", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Europe/Madrid")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    # Neofetch
    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 7, contin=True)
    t.delete_row(7, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 7, count=3, contin=True)
    t.gen_typing_text(" -u osw4l", 7, contin=True)

    git_user_details = gifos.utils.fetch_github_stats("osw4l")

    t.clear_frame()

    user_details_lines = f"""
    \x1b[30;102mosw4l@GitHub\x1b[0m
    --------------
    \x1b[96mRole:     \x1b[93mSenior Backend Engineer & Tech Lead\x1b[0m
    \x1b[96mCompany:  \x1b[93mCapytop LLC (Director of Engineering)\x1b[0m
    \x1b[96mProject:  \x1b[93mFlickFlow - Trading SaaS\x1b[0m
    \x1b[96mLocation: \x1b[93mBarcelona, Spain\x1b[0m
    \x1b[96mExp:      \x1b[93m11+ years\x1b[0m
    \x1b[96mStack:    \x1b[93mPython | Go | Elixir | Rust\x1b[0m
    \x1b[96mAI:       \x1b[93mLangChain | LangGraph | RAG | MCP\x1b[0m

    \x1b[30;102mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mRating:       \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mStars:        \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mCommits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mPRs:          \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %:  \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mContribs:     \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Langs:    \x1b[93mPython, Go, Elixir\x1b[0m
    """

    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u osw4l", 1, contin=True)

    t.toggle_show_cursor(False)
    t.gen_text(user_details_lines, 3, 1, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.toggle_show_cursor(True)
    t.gen_typing_text(
        "\x1b[92m# Open to remote | Senior/Staff Backend | AI Engineering",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()
