from src.pipelines.cesv_file_migration_pipeline import CesvFileMigration

if __name__ == '__main__':
    migration = CesvFileMigration()
    migration.execute()
