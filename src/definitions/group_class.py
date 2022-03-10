from enum import Enum


class TicketClasses(Enum):
    rest = '0'
    billing = '1'
    customer_care = '2'
    development = '3'
    dev_ateam = '4'
    dev_avengers = '5'
    dev_gondor = '6'
    dev_mordor = '7'
    dev_plugins = '8'
    dev_be = '9'
    dev_fe = '10'
    dev_triage = '11'
    first_resp = '12'
    internal = '13'


CLASS_DIRECT = {
    "Billing": TicketClasses.billing,
    "Customer Care": TicketClasses.customer_care,
    "Dev-A-Team": TicketClasses.dev_ateam,
    "Dev-Avengers": TicketClasses.dev_avengers,
    "Dev-Gondor": TicketClasses.dev_gondor,
    "Dev-Mordor": TicketClasses.dev_mordor,
    "Dev-Plugins": TicketClasses.dev_plugins,
    "Devs - BE": TicketClasses.dev_be,
    "Devs - FE": TicketClasses.dev_fe,
    "Devs-Triage": TicketClasses.dev_triage,
    "FirstResponders": TicketClasses.first_resp,
    "Internal": TicketClasses.internal,
}

# L1 is development vs. rest
CLASS_L1 = {
    "Billing": TicketClasses.rest,
    "Customer Care": TicketClasses.rest,
    "Dev-A-Team": TicketClasses.development,
    "Dev-Avengers": TicketClasses.development,
    "Dev-Gondor": TicketClasses.development,
    "Dev-Mordor": TicketClasses.development,
    "Dev-Plugins": TicketClasses.development,
    "Devs - BE": TicketClasses.development,
    "Devs - FE": TicketClasses.development,
    "Devs-Triage": TicketClasses.development,
    "FirstResponders": TicketClasses.rest,
    "Internal": TicketClasses.rest,
}

# L2 is dev_be, dev_fe vs. rest
CLASS_L2 = {
    "Billing": TicketClasses.rest,
    "Customer Care": TicketClasses.rest,
    "Dev-A-Team": TicketClasses.dev_be,
    "Dev-Avengers": TicketClasses.dev_fe,
    "Dev-Gondor": TicketClasses.dev_fe,
    "Dev-Mordor": TicketClasses.dev_fe,
    "Dev-Plugins": TicketClasses.dev_fe,
    "Devs - BE": TicketClasses.dev_be,
    "Devs - FE": TicketClasses.dev_fe,
    "Devs-Triage": TicketClasses.rest,
    "FirstResponders": TicketClasses.rest,
    "Internal": TicketClasses.rest,
}

# L3 is dev_ateam, dev_avengers, dev_gondor, dev_mordor, dev_plugins, dev_fe vs. rest
CLASS_L3 = {
    "Billing": TicketClasses.rest,
    "Customer Care": TicketClasses.rest,
    "Dev-A-Team": TicketClasses.dev_ateam,
    "Dev-Avengers": TicketClasses.dev_avengers,
    "Dev-Gondor": TicketClasses.dev_gondor,
    "Dev-Mordor": TicketClasses.dev_mordor,
    "Dev-Plugins": TicketClasses.dev_plugins,
    "Devs - BE": TicketClasses.dev_ateam,
    "Devs - FE": TicketClasses.dev_fe,
    "Devs-Triage": TicketClasses.rest,
    "FirstResponders": TicketClasses.rest,
    "Internal": TicketClasses.rest,
}
