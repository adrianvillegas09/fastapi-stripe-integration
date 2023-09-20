from app.services.stripe.charge import StripeCharge


def get_charges_dependency(limit, starting_after=None):
    charge = StripeCharge()
    return charge.get_charge_list(limit, starting_after=None)


def create_charge_dependency(amount, card, currency, description=None):
    charge = StripeCharge()
    return charge.create_charge(amount, card, currency, description=description)


def capture_charge_dependency(charge_id):
    charge = StripeCharge()
    return charge.capture_charge(charge_id)
