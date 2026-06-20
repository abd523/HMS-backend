from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        # DB was created with legacy columns (amount, is_paid) while 0001_initial
        # already recorded the new schema. Recreate table to match the model.
        migrations.RunSQL(
            sql="""
                DROP TABLE IF EXISTS billing_invoice CASCADE;
                CREATE TABLE billing_invoice (
                    id BIGSERIAL PRIMARY KEY,
                    total_amount NUMERIC(10, 2) NOT NULL,
                    status VARCHAR(20) NOT NULL DEFAULT 'Unpaid',
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                    paid_at TIMESTAMPTZ NULL,
                    patient_id BIGINT NOT NULL
                        REFERENCES patients_patient(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED
                );
                CREATE INDEX billing_invoice_patient_id_idx ON billing_invoice (patient_id);
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
