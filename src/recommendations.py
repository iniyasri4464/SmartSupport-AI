
def get_solution(category, complaint=""):

    text = complaint.lower()

    # Billing recommendations
    if category == "Billing":

        if "double" in text or "twice" in text:
            return (
                "You may have been charged twice. "
                "Please check your transaction history "
                "and contact the billing team."
            )

        elif "refund" in text:
            return (
                "Please check your refund status using "
                "your transaction ID."
            )

        elif "payment" in text:
            return (
                "Please verify your payment status and "
                "transaction ID."
            )

        return "Please verify your billing history and contact support."

    # Account recommendations
    elif category == "Account":

        if "password" in text:
            return "Please use the Forgot Password option to reset your password."

        elif "locked" in text or "unlock" in text:
            return "Please contact the account administrator to unlock your account."

        elif "login" in text or "log in" in text:
            return "Please verify your login credentials and try again."

        return "Please check your account details or contact support."

    # Order recommendations
    elif category == "Order":

        if "not arrived" in text or "not received" in text:
            return "Please check your tracking status using your order ID."

        elif "wrong item" in text:
            return "Please raise a replacement request with your order details."

        elif "cancel" in text:
            return "Please check whether your order is eligible for cancellation."

        return "Please check your order status using your order ID."

    # Network recommendations
    elif category == "Network":

        if "slow" in text:
            return "Please restart your router and check your internet speed."

        elif "disconnect" in text:
            return "Please check your network stability and router connection."

        elif "wifi" in text:
            return "Please reconnect to your Wi-Fi network and restart your router."

        return "Please check your internet connection and network settings."

    # Technical recommendations
    elif category == "Technical":

        if "crash" in text or "freez" in text:
            return "Please restart the application and check for available updates."

        elif "printer" in text:
            return "Please check the printer connection, paper supply, and driver."

        elif "laptop" in text:
            return "Please restart your laptop and check for system updates."

        return "Please restart the application and contact technical support if the issue continues."

    return "Please contact customer support for further assistance."
