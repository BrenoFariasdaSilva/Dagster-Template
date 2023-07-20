import pandas as pd

class Extraction:
    def __init__(
        self, start, end, version="v2", code="4507490", pagesize=10000, covid="False"
    ):
        self.url = f"https://www.governotransparente.com.br/transparencia/api"
        self.version = version
        self.code = code
        self.pagesize = pagesize
        self.start = start
        self.end = end
        self.covid = covid

    def get_info(self, appendix, code_before=False):
        if (code_before == True):
            return pd.read_json(f"{self.url}/{self.version}/json/{self.code}/{appendix}")
        else:
            return pd.read_json(f"{self.url}/{self.version}/json/{appendix}/{self.code}")
        # print(f"{self.url}/{self.version}/json/{self.code}/{appendix}")

    def get_iterated_info(self, data, appendix):
        df = pd.DataFrame()
        for i, r in data.iterrows():
            temp_data = pd.read_json(f"{self.url}/{self.version}/json/{self.code}/{appendix}/{i}")
            df = pd.concat([df, temp_data])
        return df