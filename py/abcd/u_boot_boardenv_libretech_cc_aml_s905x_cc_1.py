env__mmc_dev_configs = (
    {
        'fixture_id': 'sd',
        'is_emmc': False,
        'devid': 0,
        'partid': None,
        'info_device': 'mmc@72000',
        'info_speed': '50000000',
        'info_mode': 'SD High Speed (50MHz)',
        'info_buswidth': '4-bit',
    },
)

env__mmc_rd_configs = (
    {
        'fixture_id': 'sd',
        'is_emmc': False,
        'devid': 0,
        'partid': None,
        'sector': 0,
        'count': 100,
        'crc32': 'bfbeb86e',
    },
)

env__mmc_wr_configs = (
    {
        "fixture_id": "sd",
        "is_emmc": False,
        "devid": 0,
        "partid": None,
        "sector": 0x1000,
        "count": 1000,
        "test_iterations": 50,
    },
)

# checks max gpios on both bank
# toggles the led gpio
# gets a gpio at 1 (AO2) and a gpio a 0 (AO3)
env__gpio_dev_config = {
        'gpio_str_count':2 ,
        'gpio_str_1': 'aobus-banks9',
        'gpio_str_2': 'periphs-banks99',
        'gpio_op_pin': 'aobus-banks2',
        'gpio_ip_pin_set':'aobus-banks2',
        'gpio_ip_pin_clear':'aobus-banks3',
        'gpio_clear_value': 'value is 0',
        'gpio_set_value': 'value is 1',
}
