#!/env/bin/ python3

# constant for widgets weighs 75 gram
WIDGET_WEIGHS = 75
# constant for gizmo weighs 112 gram
GIZMO_WEIGHS = 112


def main():
    print("============================================")
    print("Welcome Calculator total weight of the order")
    print("============================================")
    
    choice = "y"
    while choice.lower() == "y":
        n_widgets = float(input("Enter the number of widgets: \t"))
        n_gizmos = float(input("Enter the number of gizmos: \t"))
       
        # calculate the total of weighs of widgets
        t_w_widgets = n_widgets * WIDGET_WEIGHS
        
        # calculate the total of weighs of gizmos
        t_w_gizmos = n_gizmos * GIZMO_WEIGHS
        
        # total weighs
        total_weighs = t_w_widgets + t_w_gizmos
        
        print("------------------------------------------")
        print(f"total weight of the order:\t{total_weighs:.2f}")
        print("------------------------------------------")
        choice = str(input("Continue? (y/n): ")).lower()
        
        print()
    print("Bye!")

if __name__ == "__main__":
    main()