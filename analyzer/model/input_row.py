from enum import Enum
from .base_row import BaseRow


class InputRow(BaseRow):
    """
        Class used to represent input data, which category will be assigned

    Attributes:
        name(str): entity name
        nip(str): entity nip number
        company_name_in_crm(str): entity name in database
        category(Category): final category as a result of calculations
        engagements(list): list of entity engagements
        proposals(list): list of entity proposals
        bda(list): list of entity bda
    """

    COLUMN_NAMES = ["NAME", "NIP", "NAME_IN_CRM", "CATEGORY"]

    def __init__(self, name="", nip="", company_name_in_crm=""):
        self.name = name
        self.nip = nip
        self.category = Category.NOT_ASSIGNED
        self.company_name_in_crm = company_name_in_crm
        self.engagements = []
        self.proposals = []
        self.bda = []
        self.campaigns = []

    def __str__(self):
        return "[{0.name}][{0.nip}][{0.category}][{0.company_name_in_crm}]".format(self)

    def has_any_engagements(self):
        return len(self.engagements) != 0

    def has_any_proposals(self):
        return len(self.proposals) != 0

    def has_any_bdas(self):
        return len(self.bda) != 0

    def has_any_campaigns(self):
        return len(self.campaigns) != 0

    def is_entity_name_same_as_crm_name(self, entity_name):
        return entity_name.upper() == self.company_name_in_crm.upper()

    def print_attributes_separated_by_semicolon(self):
        return "{0.name};{0.nip};{0.company_name_in_crm};{0.category}".format(self)

    def get_column_values_as_list(self):
        return [self.name, self.nip, self.company_name_in_crm, self.category]

    def get_engagements_column_values(self):
        all_engagements_data = []

        for engagement in self.engagements:
            engagement_data = engagement.get_column_values_as_list()
            all_engagements_data.append(engagement_data)

        return all_engagements_data

    def get_proposals_column_values(self):
        all_proposals_data = []

        for proposal in self.proposals:
            proposal_data = proposal.get_column_values_as_list()
            all_proposals_data.append(proposal_data)

        return all_proposals_data

    def get_bda_column_values(self):
        all_bda_data = []

        for row in self.bda:
            bda_data = row.get_column_values_as_list()
            all_bda_data.append(bda_data)

        return all_bda_data


class Category(Enum):

    NOT_ASSIGNED = 0
    ACCEPTED = 1
    TO_CHECK = 2
    NOT_ACCEPTED = 3
