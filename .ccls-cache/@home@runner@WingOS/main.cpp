#include <iostream>
#include <fstream>
#include <string>
int main() {
    int instructionPointer = 1;
    int iteration = 0;
    std::string data = "bios.bootlog: Start Sequence Success: True;";

    while (true) {
        switch (instructionPointer) {
            case 1: {
                iteration++;
                instructionPointer = 3;
                if (iteration >= 2) {
                    instructionPointer = 2; // Jump to instruction 2 after 2 iterations of this instruction
                    iteration = 0;
                }
                break;
            }
            case 2: {
                std::cout << "OS BOOT" << std::endl;
                const char* command = "python3 WingOS/main.py";

                int returnCode = std::system(command);

                if (returnCode == 0) {
                    std::cout << "OS BOOT SUCCESS" << std::endl;
                } else if (returnCode == 1) {
                    std::cout << "Process Exited using Keyboard interupt" << std::endl;
                } else if (returnCode == 2) {
                    std::cout << "Import Error found" << std::endl;
                } else {
                    std::cout << "OS Fail Load: Python/C++ Error: " << returnCode << std::endl;
                }
                instructionPointer = 4; // Jump to instruction 4
                break;
            }
            case 3: {
                // Write data to a file
                std::ofstream file("data.txt");
                if (file.is_open()) {
                    file << data;
                    file.close();
                } else {
                    std::cout << "Error: Unable to open the file for writing." << std::endl;
                }
                instructionPointer = 1;
                break;
            }
            case 4: {
                std::cout << "Program exit." << std::endl;
                return 0; // Exit the program
            }
            default: {
                std::cout << "Invalid instruction: " << instructionPointer << std::endl;
                return 1; // Error: Unknown instruction
            }
        }
    }
    return 0;
}
