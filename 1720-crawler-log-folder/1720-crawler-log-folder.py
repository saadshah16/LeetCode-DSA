class Solution:
    def minOperations(self, logs: List[str]) -> int:
        Main_Folder = 0
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                Main_Folder = max(0, Main_Folder-1)
            else:
                Main_Folder += 1
        
        if Main_Folder < 0:
            return 0
        else:
            return Main_Folder

