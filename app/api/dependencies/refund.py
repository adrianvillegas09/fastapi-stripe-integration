from app.services.stripe.refund import StripeRefund


def create_refund_dependency(charge_id):
    charge = StripeRefund()
    return charge.create_refund(charge_id)
