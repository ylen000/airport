from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime

class AirportMedical(models.Model):
    _name = 'airport.medical'
    _description = 'Airport medical visit model'

    name = fields.Char(string='姓名')
    birthday = fields.Date(string='生日')
    sex_id = fields.Many2one('airport.medical.sex', string='性別')
    come_reason_id = fields.Many2one('airport.medical.come', string='為何至機場')
    nationality_id = fields.Many2one('airport.medical.nationality', string='國籍')
    race_id = fields.Many2one('airport.medical.race', string='種族')
    airport_co_id = fields.Many2one('airport.medical.company', string='航空公司')
    departure_id = fields.Many2one('airport.medical.departure', string='啟程地')
    passing_id = fields.Many2one('airport.medical.passing', string='經過地')
    arrival_id = fields.Many2one('airport.medical.arrival', string='目的地')
    patient_name =fields.Char(string='病患姓名')
    nationality_id = fields.Many2one('airport.medical.nationality', string='國籍')
    sex_id = fields.Many2one('airport.medical.sex', string='性別')
    birthday = fields.Date(default=lambda self: fields.Date.today(), string='生日')
    airport_co_id = fields.Many2one('airport.medical.company', string='航空公司')
    flight_number = fields.Char(string='班機')
    incident_date = fields.Date(default=lambda self: fields.Date.today(), string='事發日期')
    incident_place_id = fields.Many2one('airport.medical.incident.place', string='事故地點')
    notify_staff = fields.Char(string='通報人員')
    immigration_status1 = fields.Boolean(string='出境')
    immigration_status2 = fields.Boolean(string='入境')
    immigration_status3 = fields.Boolean(string='過境')
    initial_diagnosis = fields.Text(string='初步診斷')
    follow_up_results = fields.Selection(string='後續結果',selection=[('自行返家', '自行返家'), ('繼續搭機', '繼續搭機'), ('轉送至', '轉送至:'), ('醫療中心觀察', '醫療中心觀察'), ('空跑', '空跑'), ('其他', '其他')],
        help="Type is used to separate Leads and Opportunities")
    follow_up_results_replenish = fields.Char(string=' ')
    medical_bills = fields.Char(string='醫療費用收費', readonly=True)
    medical_bills_yes = fields.Boolean(string='是')
    medical_bills_no = fields.Boolean(string='否')
    charge_amount = fields.Char(string='收費金額')
    T1_telephone_number_of_Operation_Safety_Department = fields.Boolean(string='T1-032733578')
    T2_telephone_number_of_Operation_Safety_Department = fields.Boolean(string='T2-032733367')
    Medical_Center_T1_Telephone = fields.Boolean(string='T1-033834225')
    Medical_Center_T2_Telephone = fields.Boolean(string='T2-033983485')
    incident_time_id = fields.Many2one('airport.medical.incident.time', string='事發時段')
    chief_complaint_id = fields.Many2one('airport.medical.chief.complaint', string='主訴')
    diagnosis_id = fields.Many2one('airport.medical.diagnosis', string='診斷')
    treatment_id = fields.Many2one('airport.medical.treatment', string='處置')
    result_id = fields.Many2one('airport.medical.result', string='結果')
    treatment_hospital_id = fields.Many2one('airport.medical.treatment.hospital', string='若在醫院的處置')
    personal_opinion = fields.Text(string='個人意見')
    notification_time = fields.Datetime(default=lambda self: fields.Datetime.now(), string='通報時間')
    clinic_time = fields.Datetime(default=lambda self: fields.Datetime.now(), string='診療時間')
    attending_physician_id = fields.Many2one('airport.medical.attending.physician', string='負責醫師')
    attending_nurse_id = fields.Many2one('airport.medical.attending.nurse', string='隨行護士')
    test1 = fields.Char(string='test')
    identity_id = fields.Many2one('airport.medical.identity', string='身分')
    password_no = fields.Char(string='護照號碼')
    Date = fields.Date(default=lambda self: fields.Date.today(), string='日期')
    Address = fields.Char(string='地址')
    Phone = fields.Char(string='聯絡電話')
    Airplane = fields.Char(string='班機')
    exit_id  = fields.Many2one('airport.medical.exit', string='出入境')
    content= fields.Text(string='內容')
    current_time = fields.Datetime(string='紀錄時間', default=datetime.datetime.now(), readonly=True)
    display_content = fields.Text(string='紀錄內容', readonly=True)
    def record(self):
        self.display_content = self.content
    def reset(self):
        self.content = False
    doctor_remark = fields.Char(string='醫師囑言及備註')
    diagnosis_category = fields.Many2one('airport.medical.diagnosis', string='')
    diagnosis_detail = fields.Many2one('airport.medical.diagnosis')
    comment_id= fields.Many2one('airport.medical.comment', string='醫師囑言')
    comment2= fields.Many2one('airport.medical.comment')
    comment3= fields.Many2one('airport.medical.comment')
    assist_screening_id = fields.Many2one('airport.medical.assist.screening', string='協助篩檢')
    temperature = fields.Float(string='體溫', digits=(2, 1))
    temperature_status = fields.Char(string='體溫狀態', compute='_compute_temperature_status', store=True)
    @api.onchange('temperature')
    def _onchange_temperature(self):
        if self.temperature and int(self.temperature) > 99:
            raise ValidationError('不能輸入超過兩位整數！')
    @api.depends('temperature')
    def _compute_temperature_status(self):
        for record in self:
            if record.temperature and record.temperature <= 37.5:
                record.temperature_status = '體溫正常'
            elif record.temperature and record.temperature > 37.5:
                record.temperature_status = '體溫異常'
            else:
                record.temperature_status = ''
    pulse = fields.Char(string='脈搏')
    breath = fields.Char(string='呼吸')
    blood_pressureh = fields.Char(string='血壓')
    blood_oxygen = fields.Char(string='血氧') 
    consciousness = fields.Char(string='意識', readonly=True) 
    allergy = fields.Char(string='藥物過敏', readonly=True) 
    is_active1 = fields.Boolean(string='Clear')
    is_active2 = fields.Boolean(string='GCS')
    is_active3 = fields.Boolean(string="無")
    is_active4 = fields.Boolean(string="有")
    input_field = fields.Char(string="藥物名稱")
    head = fields.Char(string="頭頸部")
    chest = fields.Char(string="胸部")
    abdomen = fields.Char(string="腹部")
    limbs = fields.Char(string="四肢")
    other = fields.Char(string="其他")
    
    
    