from stock_api import fetch_stock_history, calculate_changes
from ui import print_stock_info, print_error, RESET
from AI_News import print_news
from Portfolio import buy_stock, sell_stock, show_history, remove_last, show_portfolio


def process_input(user_input):
    parts = user_input.split()
    symbol = parts[0].upper()
    flags = parts[1:] if len(parts) > 1 else []
    
    print(f"Fetching stock price for {symbol}...")
    
    history = fetch_stock_history(symbol)
    if history is None or history.empty:
        print_error(f"No data found for {symbol.upper()}. Please check the symbol and try again.")
        return

    stock_data = calculate_changes(history)
    print_stock_info(symbol, stock_data)
    NEWS = "-NEWS" == flags[0] if flags else False
    print_news(NEWS, symbol)

if __name__ == "__main__":
    try:
        welcome = "WELCOME TO THE TERMINAL STOCK TRACKER!"
        help_hint = "TYPE 'HELP' FOR AVAILABLE COMMANDS"
        print(f"\n{welcome.center(50)}")
        print(f"{help_hint.center(50)}\n")
        while True:
            cmd = input("Enter a command or US stock ticker: ").strip()
            parts = cmd.split()

            if not parts:
                continue
            command = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []

            if command in ['exit', 'quit', 'q']:
                print("Exiting the stock tracker. Goodbye!")
                break

            elif command == "help":
                header = "AVAILABLE COMMANDS"
                print(f"\n{header.center(70)}")
                print("=" * 80)
                print(f"\033[93m    {'<Ticker>':<30}{RESET} : Fetch stock information for a ticker\n")
                print(f"\033[93m    {'<Ticker> -NEWS':<30}{RESET} : Fetch stock info + AI news summary\n")
                print(f"\033[93m    {'BUY <Ticker> <Amount> <Price>':<30}{RESET} : Add a BUY transaction\n")
                print(f"\033[93m    {'SELL <Ticker> <Amount> <Price>':<30}{RESET} : Add a SELL transaction\n")
                print(f"\033[93m    {'PORTFOLIO':<30}{RESET} : Show current holdings and performance\n")
                print(f"\033[93m    {'HISTORY':<30}{RESET} : Show transaction history\n")
                print(f"\033[93m    {'REMOVE':<30}{RESET} : Remove last transaction (undo)\n")
                print(f"\033[93m    {'HELP':<30}{RESET} : Show this help menu\n")
                print(f"\033[93m    {'EXIT / QUIT / Q':<30}{RESET} : Exit the program\n")
                print("=" * 80)
                print("\n    EXAMPLES:")
                print("     VOO")
                print("     VOO -NEWS")
                print("     BUY VOO 1.57 593.32")
                print("     SELL VOO 0.50 615.10")
                print("     PORTFOLIO")
                print("     REMOVE")
                print("     HISTORY\n")
                print("=" * 80)
                print("\n")

            elif command == "buy" and len(args) == 3:
                ticker, qty, price = args[0], round(float(args[1]), 4), round(float(args[2]), 2)
                buy_stock(ticker, qty, price)

            elif command == "sell" and len(args) == 3:
                ticker, qty, price = args[0], round(float(args[1]), 4), round(float(args[2]), 2)
                sell_stock(ticker, qty, price)

            elif command == "history":
                show_history()

            elif command == "remove":
                remove_last()

            elif command == "portfolio":
                show_portfolio()

            elif cmd:
                process_input(cmd)
    except KeyboardInterrupt:
        print("\nExiting the stock tracker. Goodbye!")
