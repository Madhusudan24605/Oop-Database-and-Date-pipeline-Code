class FileHandler:
    filepath: str # indicate that filepath is a string type
    def __init__(self, filepath: str):
        self.filepath = filepath
        return None
    
    def read(self) -> list [str]:
        rows: list [str] = []
        try:
            filehandle = open(self.filepath, 'r', encoding='utf-8')
            rows = filehandle.readlines()
            while rows != '':
                rows.append(rows.strip())
                rows = filehandle.readlines()
                filehandle.close()
        except Exception:
            print(f'File not found')
            
        return rows
