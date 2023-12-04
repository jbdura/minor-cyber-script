import os
import hashlib
import platform  
import socket 


class SystemInformationRetrieval:
    def __init__(self):
        self.os_version = platform.system()
        self.installed_software = list(os.listdir('/usr/bin'))
        self.network_configurations = socket.gethostbyname(
            socket.gethostname())  # Modify this line for specific for more detailed network information
        self.user_privileges = os.getuid()


    def get_os_version(self):
        return self.os_version

    def get_installed_software(self):
        return self.installed_software

    def get_network_configurations(self):
        return self.network_configurations

    def get_user_privileges(self):
        return self.user_privileges


class CommandMonitoring:
    def __init__(self):
        self.whitelist = ['ls', 'pwd', 'mkdir', 'rmdir']

    def monitor_commands(self):
        while True:
            command = input("Enter a command: ")

            if command not in self.whitelist:
                print("Warning: Suspicious command detected:", command)

            else:
                print("Command executed:", command)


class CountermeasureSuggestion:
    def __init__(self):
        pass

    def suggest_countermeasures(self, threat):
        if threat == "Malware injection":
            print("Recommendation: Enable whitelisting for command execution.")

        elif threat == "Unrestricted file transfer":
            print("Recommendation: Implement file upload/download restrictions.")

        elif threat == "Lack of file integrity checking":
            print("Recommendation: Implement file integrity checking mechanisms.")


class FileIntegrityCheck:
    def __init__(self):
        self.file_hash = None

    def calculate_hash(self, filename):
        with open(filename, 'rb') as f:
            hasher = hashlib.sha256()
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)

        self.file_hash = hasher.hexdigest()

    def verify_integrity(self, filename):
        with open(filename, 'rb') as f:
            hasher = hashlib.sha256()
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)

        if hasher.hexdigest() == self.file_hash:
            print("File integrity verified:", filename)

        else:
            print("File integrity compromised:", filename)


if __name__ == "__main__":
    # Retrieve system information
    system_information = SystemInformationRetrieval()
    print("Operating System Version:", system_information.get_os_version())
    print("Installed Software:", system_information.get_installed_software())
    print("Network Configurations:",
        system_information.get_network_configurations())
    print("User Privileges:", system_information.get_user_privileges())

    # Monitor commands
    command_monitoring = CommandMonitoring()
    command_monitoring.monitor_commands()

    # Suggest countermeasures
    countermeasure_suggestion = CountermeasureSuggestion()
    # Simulate a threat detection
    threat = "Malware injection"
    countermeasure_suggestion.suggest_countermeasures(threat)

    # Perform file integrity check
    file_integrity_check = FileIntegrityCheck()
    # Simulate file integrity check for a specific file
    filename = "important_file.txt"
    file_integrity_check.calculate_hash(filename)
    file_integrity_check.verify_integrity(filename)
    