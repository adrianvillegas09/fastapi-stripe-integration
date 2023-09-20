from stripe import Refund

from app.core.config import STRIPE_SECRET_KEY


class StripeRefund:

    api_key = STRIPE_SECRET_KEY

    def create_refund(self, charge_id) -> Refund:
        """
        Refund a charge.

        Args:
            charge_id: object ID of the charge that needs to be refunded.

        Returns:
            A Refund object.
        """
        return Refund.create(charge=charge_id, api_key=self.api_key)
