from django.db import models

# Create your models here.
#class Snippet(models.Model):
 #   report=models.TextField()
  #  def __str__(self):
   #     return self.report

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Client(models.Model):
    fullname = models.CharField(db_column='Fullname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=20, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=20, blank=True, null=True)  # Field name made lowercase.
    room_number = models.CharField(db_column='Room_Number', max_length=5, blank=True, null=True)  # Field name made lowercase.
    client_id = models.CharField(db_column='Client_ID', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client_side'


class Closure(models.Model):
    closure_date = models.DateField(db_column='Closure_Date', blank=True, null=True)  # Field name made lowercase.
    closure_time = models.TimeField(db_column='Closure_Time', blank=True, null=True)  # Field name made lowercase.
    workaround_type = models.CharField(db_column='Workaround_Type', max_length=7, blank=True, null=True)  # Field name made lowercase.
    workaround_note = models.CharField(db_column='Workaround_Note', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'closure'


class Communication(models.Model):
    sender = models.CharField(db_column='Sender', max_length=30, blank=True, null=True)  # Field name made lowercase.
    intended_receiver = models.CharField(db_column='Intended_Receiver', max_length=30, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication'


class Cost(models.Model):
    direct_product_cost = models.FloatField(db_column='Direct_Product_Cost', blank=True, null=True)  # Field name made lowercase.
    direct_labour_cost = models.FloatField(db_column='Direct_Labour_Cost', blank=True, null=True)  # Field name made lowercase.
    direct_expense_cost = models.FloatField(db_column='Direct_Expense_Cost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cost'


class Escalation(models.Model):
    escalated_from_unit = models.CharField(db_column='Escalated_From_Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    escalated_to_unit = models.CharField(db_column='Escalated_To_Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    escalated_from_technician = models.CharField(db_column='Escalated_From_Technician', max_length=30, blank=True, null=True)  # Field name made lowercase.
    escalation_date = models.DateField(db_column='Escalation_Date', blank=True, null=True)  # Field name made lowercase.
    escalation_time = models.TimeField(db_column='Escalation_Time', blank=True, null=True)  # Field name made lowercase.
    attempted_resolution_summary = models.CharField(db_column='Attempted_Resolution_Summary', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'escalation'


class History(models.Model):
    incident_reported_date = models.DateField(db_column='Incident_Reported_Date', blank=True, null=True)  # Field name made lowercase.
    incident_reported_hour = models.TimeField(db_column='Incident_Reported_Hour', blank=True, null=True)  # Field name made lowercase.
    ticket_age = models.DateTimeField(db_column='Ticket_Age', blank=True, null=True)  # Field name made lowercase.
    aging_status = models.CharField(db_column='Aging_Status', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'history'


class Impact(models.Model):
    impact_code = models.AutoField(db_column='Impact_Code', primary_key=True)  # Field name made lowercase.
    impact_summary = models.CharField(db_column='Impact_Summary', max_length=100, blank=True, null=True)  # Field name made lowercase.
    severe_status = models.CharField(db_column='Severe_Status', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'impact'


class It(models.Model):
    it_sub_unit_name = models.CharField(db_column='IT_Sub_Unit_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contact_person = models.CharField(db_column='Contact_Person', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', primary_key=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'it'


class Location(models.Model):
    location_id = models.CharField(db_column='Location_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=40, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=40, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=40, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=40, blank=True, null=True)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=40, blank=True, null=True)  # Field name made lowercase.
    room_number = models.CharField(db_column='Room_Number', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class Login(models.Model):
    username = models.CharField(db_column='Username', max_length=30, blank=True, null=True)  # Field name made lowercase.
    client_password = models.CharField(db_column='Client_Password', max_length=30, blank=True, null=True)  # Field name made lowercase.
    account_type = models.CharField(db_column='Account_Type', max_length=8, blank=True, null=True)  # Field name made lowercase.
    user_category = models.CharField(db_column='User_Category', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login'


class NonIt(models.Model):
    contact_person = models.CharField(db_column='Contact_Person', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'non_it'


class Organizationhaslocation(models.Model):
    subject = models.CharField(db_column='Subject', max_length=20, blank=True, null=True)  # Field name made lowercase.
    predicate = models.CharField(db_column='Predicate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    object = models.CharField(db_column='Object', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organizationhaslocation'


class PainValueAnalysis(models.Model):
    number_of_related_incidents = models.IntegerField(db_column='Number_of_Related_Incidents', blank=True, null=True)  # Field name made lowercase.
    last_reported_date = models.DateTimeField(db_column='Last_Reported_Date', blank=True, null=True)  # Field name made lowercase.
    pain_value = models.FloatField(db_column='Pain_Value', blank=True, null=True)  # Field name made lowercase.
    weighting_factor = models.CharField(db_column='Weighting_Factor', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pain_value_analysis'


class Performance(models.Model):
    resolution_time = models.DateTimeField(db_column='Resolution_Time', blank=True, null=True)  # Field name made lowercase.
    remediation_time = models.DateTimeField(db_column='Remediation_Time', blank=True, null=True)  # Field name made lowercase.
    escalation_time = models.DateTimeField(db_column='Escalation_Time', blank=True, null=True)  # Field name made lowercase.
    incident_age = models.DateTimeField(db_column='Incident_Age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'performance'


class Problem(models.Model):
    problem_code = models.AutoField(db_column='Problem_Code', primary_key=True)  # Field name made lowercase.
    problem_start_date = models.DateField(db_column='Problem_Start_Date', blank=True, null=True)  # Field name made lowercase.
    problem_end_date = models.DateField(db_column='Problem_End_Date', blank=True, null=True)  # Field name made lowercase.
    problem_summary = models.CharField(db_column='Problem_Summary', max_length=50, blank=True, null=True)  # Field name made lowercase.
    problem_category = models.CharField(db_column='Problem_Category', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'problem'


class Remediation(models.Model):
    temporary_fix_note = models.CharField(db_column='Temporary_Fix_Note', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remediation_date = models.DateField(db_column='Remediation_Date', blank=True, null=True)  # Field name made lowercase.
    remediation_time = models.TimeField(db_column='Remediation_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'remediation'


class Request(models.Model):
    request_date = models.DateField(db_column='Request_Date', blank=True, null=True)  # Field name made lowercase.
    request_time = models.TimeField(db_column='Request_Time', blank=True, null=True)  # Field name made lowercase.
    request_type = models.CharField(db_column='Request_Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    request_category = models.CharField(db_column='Request_Category', max_length=8, blank=True, null=True)  # Field name made lowercase.
    request_content = models.CharField(db_column='Request_Content', max_length=500, blank=True, null=True)  # Field name made lowercase.
    request_summary = models.CharField(db_column='Request_Summary', max_length=100, blank=True, null=True)  # Field name made lowercase.
    request_hierarchy_tier1 = models.CharField(db_column='Request_Hierarchy_Tier1', max_length=9, blank=True, null=True)  # Field name made lowercase.
    request_hierarchy_tier2 = models.CharField(db_column='Request_Hierarchy_Tier2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    request_hierarchy_tier3 = models.CharField(db_column='Request_Hierarchy_Tier3', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'


class Resolution(models.Model):
    property_number = models.CharField(db_column='Property_Number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    asset_category = models.CharField(db_column='Asset_Category', max_length=8, blank=True, null=True)  # Field name made lowercase.
    asset_name = models.CharField(db_column='Asset_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subpart = models.CharField(db_column='Subpart', max_length=20, blank=True, null=True)  # Field name made lowercase.
    root_cause_summary = models.CharField(db_column='Root_Cause_Summary', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operational_category_tier1 = models.CharField(db_column='Operational_Category_Tier1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    operational_category_tier2 = models.CharField(db_column='Operational_Category_Tier2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operational_category_tier3 = models.CharField(db_column='Operational_Category_Tier3', max_length=24, blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resolution_date = models.DateField(db_column='Resolution_Date', blank=True, null=True)  # Field name made lowercase.
    resolution_time = models.TimeField(db_column='Resolution_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resolution'


class Servicehasincdient(models.Model):
    subject = models.CharField(db_column='Subject', max_length=20, blank=True, null=True)  # Field name made lowercase.
    predicate = models.CharField(db_column='Predicate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    object = models.CharField(db_column='Object', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicehasincdient'


class Signup(models.Model):
    signup_date = models.DateField(db_column='Signup_Date', blank=True, null=True)  # Field name made lowercase.
    signup_time = models.TimeField(db_column='Signup_Time', blank=True, null=True)  # Field name made lowercase.
    signup_service_name = models.CharField(db_column='Signup_Service_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    signup_service_status = models.CharField(db_column='Signup_Service_Status', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'signup'


class Subjectpredicateobjecttable(models.Model):
    subject = models.CharField(db_column='Subject', max_length=40, blank=True, null=True)  # Field name made lowercase.
    predicate = models.CharField(db_column='Predicate', max_length=40, blank=True, null=True)  # Field name made lowercase.
    object = models.CharField(db_column='Object', max_length=40, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjectpredicateobjecttable'


class Subjectpredicatobject(models.Model):
    subject = models.CharField(db_column='Subject', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.SmallAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    predicate = models.CharField(db_column='Predicate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    object = models.CharField(db_column='Object', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjectpredicatobject'


class Threshold(models.Model):
    minimum_number_of_related_incidents = models.IntegerField(db_column='Minimum_Number_Of_Related_Incidents', blank=True, null=True)  # Field name made lowercase.
    maximum_number_of_related_incidents = models.IntegerField(db_column='Maximum_Number_Of_Related_Incidents', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'threshold'


class Unit(models.Model):
    unit_code = models.CharField(db_column='Unit_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    unit_name = models.CharField(db_column='Unit_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    unit_manager = models.CharField(db_column='Unit_Manager', max_length=30, blank=True, null=True)  # Field name made lowercase.
    unit_members = models.CharField(db_column='Unit_Members', max_length=150, blank=True, null=True)  # Field name made lowercase.
    number_of_employees = models.IntegerField(db_column='Number_Of_Employees', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unit'


class Workload(models.Model):
    number_of_assigned_tickets = models.IntegerField(db_column='Number_Of_Assigned_Tickets', blank=True, null=True)  # Field name made lowercase.
    number_of_working_tickets = models.IntegerField(db_column='Number_Of_Working_Tickets', blank=True, null=True)  # Field name made lowercase.
    number_of_closed_tickets = models.IntegerField(db_column='Number_Of_Closed_Tickets', blank=True, null=True)  # Field name made lowercase.
    number_of_opened_tickets = models.IntegerField(db_column='Number_Of_Opened_Tickets', blank=True, null=True)  # Field name made lowercase.
    number_of_escalated_tickets = models.IntegerField(db_column='Number_Of_Escalated_Tickets', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workload'
