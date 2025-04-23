class Cell(dict):
    def __init__(self, cellID : int, cellType : str):
        super().__init__({
            "cellID" : cellID,
            "cellType" : cellType
        })
    @classmethod
    def from_dict(cls, data: dict) -> "Cell":
        return cls(cellID=data["cellID"], cellType=data["cellType"])
    
    def get_cellID(self) -> int:
        return self["cellID"]

    def set_cellID(self, cellID: str) -> None:
        self["cellID"] = cellID

    def get_cellType(self) -> str:
        return self["cellType"]

    def set_cellType(self, cellType: str) -> None:
        self["cellType"] = cellType