# Railway Reservation System - Challenge 25

def main():
    total_seats = 50
    bookings = {}  # Dictionary to store: {booking_id: {"name": name, "age": age, "seat": seat_no}}
    next_seat = 1

    while True:
        print("\n--- RAILWAY RESERVATION SYSTEM ---")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            available = total_seats - len(bookings)
            print(f"\nAvailable Seats: {available}")

        elif choice == '2':
            if len(bookings) < total_seats:
                name = input("Enter Passenger Name: ")
                age = input("Enter Passenger Age: ")
                booking_id = f"RSV{1000 + next_seat}"
                
                bookings[booking_id] = {"name": name, "age": age, "seat": next_seat}
                print(f"\nBooking Successful! Your Booking ID is: {booking_id}")
                next_seat += 1
            else:
                print("\nError: No seats available!")

        elif choice == '3':
            bid = input("Enter Booking ID to search: ")
            if bid in bookings:
                ticket = bookings[bid]
                print(f"\n--- Ticket Details ---")
                print(f"ID: {bid}\nName: {ticket['name']}\nAge: {ticket['age']}\nSeat: {ticket['seat']}")
            else:
                print("\nInvalid Booking ID.")

        elif choice == '4':
            bid = input("Enter Booking ID to cancel: ")
            if bid in bookings:
                del bookings[bid]
                print(f"\nBooking {bid} has been cancelled.")
            else:
                print("\nInvalid Booking ID.")

        elif choice == '5':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()

