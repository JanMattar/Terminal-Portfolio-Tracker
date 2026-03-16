from stock_api import fetch_stock_history, calculate_changes
from ui import print_stock_info, print_error
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
                print(f"\n{header.center(50)}")
                print("=" * 80)
                print(f"    {'<symbol>':<20} : Fetch stock information for a given symbol\n")
                print(f"    {'<symbol> -NEWS':<20} : Fetch news related to the stock\n")
                print(f"    {'exit/quit/q':<20} : Exit the stock tracker\n")
                print(f"    {'help':<20} : Display this help message")
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
