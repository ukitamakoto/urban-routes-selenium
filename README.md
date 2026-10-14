# urban-routes-selenium

Selenium WebDriver + pytest + Page Object Model automation of **Urban Routes**, a taxi-ordering web app provided by the TripleTen QA Engineer bootcamp (Sprint 8 project).

## Scenarios

| # | Test | What it checks |
|---|---|---|
| 1 | `test_set_route` | The From and To addresses are set and read back |
| 2 | `test_select_plan` | "Call a taxi", then the Comfort tariff becomes the active one |
| 3 | `test_fill_phone_number` | Phone number plus the SMS confirmation code, read from the browser's network log |
| 4 | `test_fill_card` | A card (number + code) is added as the payment method |
| 5 | `test_comment_for_driver` | The message for the driver is kept |
| 6 | `test_order_blanket_and_handkerchiefs` | The blanket & handkerchiefs switch turns on |
| 7 | `test_order_2_ice_creams` | The ice-cream counter reaches 2 |
| 8 | `test_car_search_model_appears` | Placing the order opens the car-search modal |

The scenarios run in order, in one browser session, as the bootcamp brief required: each one continues the same taxi order.

## How it is built

- `pages.py`: the Page Object. Locators and actions in one place, with explicit waits (`WebDriverWait` + `expected_conditions`) and no sleeps.
- `data.py`: the test data.
- `helpers.py`: provided by the bootcamp. It reads the SMS code from Chrome's performance log through the DevTools protocol (`Network.getResponseBody`), which is why the driver starts with `goog:loggingPrefs = {"performance": "ALL"}`.
- `tests/test_urban_routes.py`: the 8 scenarios.

## Run it

The bootcamp served the app from a temporary per-student URL that has since expired. The suite therefore skips itself when `URBAN_ROUTES_URL` is not set.

```bash
uv sync
URBAN_ROUTES_URL="https://<your-urban-routes-instance>/" uv run pytest
```

There is no CI here because there is no server left to test against. For a suite you can run today, with CI and a public report, see [qa-automation-python](https://github.com/ukitamakoto/qa-automation-python).
