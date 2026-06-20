from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        ('accounts', '0002_auditlog'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DROP TABLE IF EXISTS doctors_doctor CASCADE;
                CREATE TABLE doctors_doctor (
                    id BIGSERIAL PRIMARY KEY,
                    specialization VARCHAR(100) NOT NULL,
                    license_number VARCHAR(50) NOT NULL UNIQUE,
                    experience_years INTEGER NOT NULL DEFAULT 0,
                    is_available BOOLEAN NOT NULL DEFAULT TRUE,
                    user_id BIGINT NOT NULL UNIQUE
                        REFERENCES accounts_user(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED
                );
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
