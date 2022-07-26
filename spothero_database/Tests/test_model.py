import spothero_database.lib.model as model


def test_new_rate():
    rate = model.Rates(
        days="thurs,fri",
        start_time="09:00:00",
        end_time="12:00:00",
        timezone="America/Chicago",
        price="1400"
    )

    assert rate.days == "thurs,fri"
    assert rate.price == "1400"

