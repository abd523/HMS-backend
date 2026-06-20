from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DROP TABLE IF EXISTS patients_patient CASCADE;
                CREATE TABLE patients_patient (
                    id BIGSERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    date_of_birth DATE NULL,
                    gender VARCHAR(1) NOT NULL,
                    phone_number VARCHAR(15) NOT NULL,
                    email VARCHAR(254) NULL,
                    address TEXT NOT NULL DEFAULT '',
                    medical_history TEXT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                );
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
