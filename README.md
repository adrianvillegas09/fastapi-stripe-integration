# python-stripe-integration

An backend with stripe payment API integration using Python(FastAPI)

1. Create charge for card payment
   - POST /api/v1/create_charge
2. Capture the created charge
   - POST /api/v1/capture_charge/:chargeId
3. Create a refund for the created charge
   - POST /api/v1/create_refund/:chargeId
4. Get a List of all charges
   - GET /api/v1/get_charges

### Using Docker

STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY
Run -

```
    make build_image
    make run_docker
```

Application is accessable in localhost:8000
