import streamlit as st


class PosApp:
    def __init__(self):
        # Initialize session state variables if they don't exist
        if 'total' not in st.session_state:
            st.session_state.total = 0.00

    def render(self):
        # Set the page title
        st.title("Point of Sale (POS) System")

        # Create an empty placeholder for the total
        total_placeholder = st.empty()

        # Display current total using the placeholder
        total_placeholder.header(f"Total Bill: £{st.session_state.total:.2f}")

        # Item price input
        item_price = st.number_input(
            "Enter Item Price (£)",
            min_value=0.00,
            format="%.2f",
            step=0.01
        )

        # Add item button
        if st.button("Add Item"):
            if item_price > 0:
                # Update total
                st.session_state.total += item_price

                # Update the total placeholder
                total_placeholder.header(
                    f"Total Bill: £{st.session_state.total:.2f}")

                # Provide feedback
                st.success(f"Added item: £{item_price:.2f}")

        # Reset button
        if st.button("Reset Bill"):
            st.session_state.total = 0.00
            total_placeholder.header(
                f"Total Bill: £{st.session_state.total:.2f}")
            st.rerun()


def main():
    app = PosApp()
    app.render()


if __name__ == "__main__":
    main()
