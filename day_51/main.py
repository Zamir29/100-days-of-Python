from internet_bot import InternetSpeedXBot
from config import (
    PROMISED_UP,
    PROMISED_DOWN,
    INTERNET_PROVIDER,
)

def main():
    bot = InternetSpeedXBot()
    down, up = bot.get_internet_speed()
    # Immediately check the result with promised threshold
    down_difference = down - PROMISED_DOWN
    up_difference = up - PROMISED_UP
    down_ok = down_difference >= 0
    up_ok = up_difference >= 0

    complaint_text = ""
    print("--------------------------\n"
          "| INTERNET SPEED SUMMARY |\n"
          "--------------------------")

    if down_ok and up_ok:
        print(f"🟢 All good!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, faster than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, faster than promised\n")
    elif down_ok and not up_ok:
        complaint_text = f"Hey {INTERNET_PROVIDER}! why is my upload speed {up:.2f} when I pay for {PROMISED_UP}?"
        print(f"🟠 Meh, it could be better!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, faster than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, lower than promised\n"
              f"\n💬 Sending complaint on x.com:\n{complaint_text}\n")
        #Maybe before sending tweet it could be a user input to confirm with y/n
        # Send the text to tweet
        bot.x_at_provider(complaint_text)
    elif not down_ok and up_ok:
        complaint_text = f"Hey {INTERNET_PROVIDER}! why is my download speed {down:.2f} when I pay for {PROMISED_DOWN}?"
        print(f"🟠 Meh, it could be better!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, lower than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, faster than promised\n"
              f"\n💬 Sending complaint on x.com:\n{complaint_text}\n")
        bot.x_at_provider(complaint_text)
    else:
        complaint_text = (f"Hey {INTERNET_PROVIDER}! "
                          f"why is my internet speed {down:.2f} down / {up:.2f}up "
                          f"when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?")
        print(f"🔴 Ehm that's not good!\n"
              f"⬇️ Your download speed ({down:.2f} Mbps) delta is: {down_difference:+.2f} Mbps, lower than promised\n"
              f"⬆️ Your upload speed ({up:.2f} Mbps) delta is: {up_difference:+.2f} Mbps, lower than promised\n"
              f"\n💬 Sending complaint on x.com:\n{complaint_text}\n")
        bot.x_at_provider(complaint_text)
    bot.driver_quit()

if __name__ == '__main__':
    main()
