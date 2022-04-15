import CMD_HELP
import owner
import CMD_HANDLER as cmd
from userbot.utils import edit_or_reply


@adam_cmd(pattern="lhelp$")
async def usit(e):
    await edit_or_reply(e,
                        f"**Halo {owner} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:\n"
                        "\n[Telegram](t.me/skyiarul)"
                        "\n[Grup Support](t.me/wibu_telegram)"
                        "\n[Repo](https://github.com/userkontol/adam-Userbot)"
                        "\n[Instagram](instagram.com/muhadam1818)")


@adam_cmd(pattern="vars$")
async def var(m):
    await edit_or_reply(m,
                        f"**Disini Daftar Vars Dari {owner}:**\n"
                        "\n[DAFTAR VARS](https://raw.githubusercontent.com/jookalem/Joo-Userbot/Joo-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    f"`{cmd}lhelp`\
\nUsage: Bantuan Untuk adam-Userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
})
