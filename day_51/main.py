from internet_bot import InternetSpeedXBot
from config import (
    PROMISED_UP,
    PROMISED_DOWN,
)

def main():
    bot = InternetSpeedXBot()
    down, up = bot.get_internet_speed()
    # Immediately check the result with promised threshold
    down_difference = down - PROMISED_DOWN
    up_difference = up - PROMISED_UP
    down_ok = down_difference >= 0
    up_ok = up_difference >= 0

    print("--------------------------\n"
          "| INTERNET SPEED SUMMARY |\n"
          "--------------------------")

    if down_ok and up_ok:
        print(f"🟢 All good!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, faster than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, faster than promised\n")
    elif down_ok and not up_ok:
        print(f"🟠 Meh, it could be better!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, faster than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, lower than promised\n"
              f"\n💬 Sending complaint on x.com:\n")
        # bot.x_at_provider()
    elif not down_ok and up_ok:
        print(f"🟠 Meh, it could be better!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, lower than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, faster than promised\n"
              f"\n💬 Sending complaint on x.com:\n")
        # bot.x_at_provider()
    else:
        print(f"🔴 Ehm that's not good!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, lower than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, lower than promised\n"
              f"\n💬 Sending complaint on x.com:\n")
        # bot.x_at_provider()

    bot.driver_quit()

if __name__ == '__main__':
    main()
