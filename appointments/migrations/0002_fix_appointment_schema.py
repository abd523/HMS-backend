from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
        ('patients', '0002_fix_patient_schema'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DROP TABLE IF EXISTS appointments_appointment CASCADE;
                CREATE TABLE appointments_appointment (
                    id BIGSERIAL PRIMARY KEY,
                    appointment_date DATE NOT NULL DEFAULT CURRENT_DATE,
                    appointment_time TIME NOT NULL DEFAULT CURRENT_TIME,
                    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
                    reason TEXT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                    doctor_id BIGINT NOT NULL
                        REFERENCES doctors_doctor(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
                    patient_id BIGINT NOT NULL
                        REFERENCES patients_patient(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED
                );
                CREATE INDEX appointments_appointment_doctor_id_idx ON appointments_appointment (doctor_id);
                CREATE INDEX appointments_appointment_patient_id_idx ON appointments_appointment (patient_id);
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
