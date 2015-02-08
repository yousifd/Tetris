// YOUSIF ALDOLAIJAN
// BILLBOARD.CPP
// ASSIGNMENT 15

#include <iostream>
#include <fstream> //used for input and output for files
#include <string>
#include <cstdlib>
#include <algorithm>

using namespace std;

//-------------------------------------------------------
//GLOBAL VARIABLES---------------------------------------
//-------------------------------------------------------
const int BILLBOARD_SIZE = 240;//the number of LEDs on the billboard
const int LETTER_SIZE = 20;//number of LEDs for each character
fstream infile ( "Billboard.dat", ios::in | ios::out );//creates file variable for use to program billboard
fstream outfile( "Billboard.out", ios::in | ios::out | ios::trunc );//creates file variable to output result
char billboard[BILLBOARD_SIZE];//stores the leds in a 1D array to easily minipulate the billboard
string part1;//stores the first part of the command
string part2;//stores the second part of the command
string type;//stores the type if mode the billboard is using
string temp;//stores the sentence for setstr() for modification during scrolling
int iter = 0;//stores the value of the current position to change in billboard
int command_num = 1;//stores the sequence number of the command

//-------------------------------------------------------
//FUNCTIONS----------------------------------------------
//-------------------------------------------------------
string readfile();//returns commands from Billboard.dat
void actions(string command);//holds the conditions with which a command is called
void clear();//clears display
void display();//display billboard
void end();//ends program
void mode();//checks the mode used to modify the billboard
void GoTo();//sets the starting position on the billboard

//SET FUNCTIONS
void setbit();//used to modify each bit of the billboard
void setchar(string letter);//used to modify the billboard with letters or numbers
void setstr();//used to modfiy the billboard with a whole string

//-------------------------------------------------------
//CHARACTERS---------------------------------------------
//-------------------------------------------------------

//-------------------------------------------------------
//LETTERS------------------------------------------------
//-------------------------------------------------------
char char_Space[LETTER_SIZE] = {'.', '.', '.', '.',
                                '.', '.', '.', '.',
                                '.', '.', '.', '.',
                                '.', '.', '.', '.',
                                '.', '.', '.', '.',};
char char_A[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '*', '*', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',};
char char_B[LETTER_SIZE] = {'*', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '*', '*', '.',};
char char_C[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '.', '.', '.',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',};
char char_D[LETTER_SIZE] = {'*', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '*', '*', '.',};
char char_E[LETTER_SIZE] = {'*', '*', '*', '*',
                            '*', '.', '.', '.',
                            '*', '*', '*', '.',
                            '*', '.', '.', '.',
                            '*', '*', '*', '*',};
char char_F[LETTER_SIZE] = {'*', '*', '*', '*',
                            '*', '.', '.', '.',
                            '*', '*', '*', '.',
                            '*', '.', '.', '.',
                            '*', '.', '.', '.',};
char char_G[LETTER_SIZE] = {'.', '*', '*', '*',
                            '*', '.', '.', '.',
                            '*', '.', '*', '*',
                            '*', '.', '.', '*',
                            '.', '*', '*', '*',};
char char_H[LETTER_SIZE] = {'*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '*', '*', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',};
char char_I[LETTER_SIZE] = {'*', '*', '*', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',
                            '*', '*', '*', '.',};
char char_J[LETTER_SIZE] = {'.', '*', '*', '*',
                            '.', '.', '*', '.',
                            '*', '.', '*', '.',
                            '*', '.', '*', '.',
                            '.', '*', '.', '.',};
char char_K[LETTER_SIZE] = {'*', '.', '*', '*',
                            '*', '*', '.', '.',
                            '*', '*', '.', '.',
                            '*', '.', '*', '.',
                            '*', '.', '.', '*',};
char char_L[LETTER_SIZE] = {'*', '.', '.', '.',
                            '*', '.', '.', '.',
                            '*', '.', '.', '.',
                            '*', '.', '.', '.',
                            '*', '*', '*', '*',};
char char_M[LETTER_SIZE] = {'*', '.', '.', '*',
                            '*', '*', '*', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',};
char char_N[LETTER_SIZE] = {'*', '.', '.', '*',
                            '*', '*', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '*', '*',
                            '*', '.', '.', '*',};
char char_O[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',};
char char_P[LETTER_SIZE] = {'*', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '*', '*', '.',
                            '*', '.', '.', '.',
                            '*', '.', '.', '.',};
char char_Q[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '*', '*',
                            '.', '*', '*', '*',};
char char_R[LETTER_SIZE] = {'*', '*', '*', '.',
                            '*', '.', '.', '*',
                            '*', '*', '*', '.',
                            '*', '.', '*', '.',
                            '*', '.', '.', '*',};
char char_S[LETTER_SIZE] = {'.', '*', '*', '*',
                            '*', '.', '.', '.',
                            '.', '*', '*', '.',
                            '.', '.', '.', '*',
                            '*', '*', '*', '.',};
char char_T[LETTER_SIZE] = {'*', '*', '*', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',};
char char_U[LETTER_SIZE] = {'*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '.', '*', '*', '*',};
char char_V[LETTER_SIZE] = {'*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',};
char char_W[LETTER_SIZE] = {'*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '*', '*', '*',
                            '*', '.', '.', '*',};
char char_X[LETTER_SIZE] = {'*', '.', '.', '*',
                            '.', '*', '*', '.',
                            '.', '.', '.', '.',
                            '.', '*', '*', '.',
                            '*', '.', '.', '*',};
char char_Y[LETTER_SIZE] = {'*', '.', '*', '.',
                            '*', '.', '*', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',};
char char_Z[LETTER_SIZE] = {'*', '*', '*', '*',
                            '.', '.', '*', '.',
                            '.', '.', '.', '.',
                            '.', '*', '.', '.',
                            '*', '*', '*', '*',};
//-------------------------------------------------------
//NUMBERS------------------------------------------------
//-------------------------------------------------------
char char_1[LETTER_SIZE] = {'.', '*', '.', '.',
                            '*', '*', '.', '.',
                            '.', '*', '.', '.',
                            '.', '*', '.', '.',
                            '*', '*', '*', '.',};
char char_2[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '.', '.', '*', '.',
                            '.', '*', '.', '.',
                            '*', '*', '*', '*',};
char char_3[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '.', '.', '*', '.',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',};
char char_4[LETTER_SIZE] = {'.', '.', '*', '.',
                            '.', '*', '*', '.',
                            '*', '*', '*', '*',
                            '.', '.', '*', '.',
                            '.', '.', '*', '.',};
char char_5[LETTER_SIZE] = {'*', '*', '*', '*',
                            '*', '.', '.', '.',
                            '*', '*', '*', '.',
                            '.', '.', '.', '*',
                            '*', '*', '*', '.',};
char char_6[LETTER_SIZE] = {'.', '.', '*', '*',
                            '.', '*', '.', '.',
                            '*', '*', '*', '.',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',};
char char_7[LETTER_SIZE] = {'*', '*', '*', '*',
                            '.', '.', '.', '.',
                            '.', '.', '*', '.',
                            '.', '*', '.', '.',
                            '*', '.', '.', '.',};
char char_8[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '.', '*', '*', '.',};
char char_9[LETTER_SIZE] = {'.', '*', '*', '.',
                            '*', '.', '.', '*',
                            '.', '*', '*', '*',
                            '.', '.', '*', '.',
                            '*', '*', '.', '.',};
char char_0[LETTER_SIZE] = {'*', '*', '*', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '.', '.', '*',
                            '*', '*', '*', '*',};

int main()
{
    string command;

    while(!infile.eof()) {
    command = readfile();
    cout << '\n' << command_num << " Command: " << command;
    cout << "\nParameter: " << part2;
    command_num++;

    actions(command);
    }

    return 0 ;
}

string readfile()
{
    string cmd;//stores the command read from the file
    unsigned found;//used to store the position of whitespace

    getline(infile, cmd);//gets the line that holds the command

    found = cmd.find_first_of(' ');

    if (cmd[found] == ' ')//check if there is a space, if so check what type fo command it contains
   {
        part1 = cmd;
        part2 = cmd;
        part1.erase(found);//stores the value of the first command
        part2.erase(0, found);//stores the value of the second command
        part2.erase(part2.begin());//removes whitespace from the begining of the parameter

        if (part1 == "MODE" || part1 == "GOTO" || part1 == "SETBIT" || part1 == "SETCHAR" || part1 == "SETSTR")
        {
            return part1;
        }
        else
        {
            cout << "\n\nERROR: WHITESPACES NOT RECONGNIZED\n\n";
        }
    }

    return cmd;
}

void actions(string command)
{
    if (command == "CLEAR")
    {
        clear();
    }
    else if (command == "DISPLAY")
    {
        display();
    }
    else if (command == "END")
    {
        end();
    }
    else if (command == "GOTO")
    {
        GoTo();
    }
    else if (command == "MODE")
    {
        mode();
    }
    else if (command == "SETBIT")
    {
        setbit();
    }
    else if (command == "SETCHAR")
    {
        setchar(part2);
    }
    else if (command == "SETSTR")
    {
        setstr();
    }
    else
    {
        cout << "\n\nERROR: INVALID COMMAND\n\n";
    }
}

void clear()
{
    for (int i = 0; i < BILLBOARD_SIZE; ++i)
    {
        billboard[i] = '.';
    }
}

void display()
{
    for (int i = 0; i < BILLBOARD_SIZE; ++i)
    {
        if (i >= 48 && (i%48) == 0)//finish the line when you get to the 48th element
        {
            outfile << endl;
        }

        outfile << billboard[i] << ' ';//displays the billboard
    }

    outfile << "\n\n";

    iter = 0;//in case you wanted to write 2 different sentences, or more than 1 board
}

void end()
{
    infile.close();
    outfile.close();
    exit(0);
}

void GoTo()
{
    if (type == "STR")
    {
        cout << "\n\nERROR: INVALID COMMAND FOR STR\n\n";
        end();
    }

    int goto_value = atoi(part2.c_str());//used to change the second string into integer
    iter = goto_value;//iterates the change in the array

    part2 = "";
}

void mode()
{
    if (part2 == "BIN" || part2 == "CHAR" || part2 == "STR")//whitespace is used since i was unable to remove it from the read file
    {
    type = part2;
    cout << "\nMode:" << type << "!!!";
    }

    part2 = "";
}

void setbit()
{
    if (type == "BIN")
    {
        if (iter > 239 || iter < 0)//incase the user inputs an invalid goto position
            {
                cout << "\n\nERROR: INVALID GOTO VALUE FOR BIT!!!\n\n";
                end();
            }
        char sign = '.';//stores the sign that will be assigned in the billboard

        if (part2 == "ON")//whitespace is used since i was unable to remove it from the read file
        {
            sign = '*';
        }
        else if (part2 == "OFF")//whitespace is used since i was unable to remove it from the read file
        {
            sign = '.';
        }
        else
        {
            cout << "\n\nERROR: SETBIT CONDITION UNDEFINED\n\n";
        }

        billboard[iter] = sign;

        ++iter;

        part2 = "";
    }
    else
    {
        cout << "\n\nERROR: WRONG MODE FOR SETBIT\n\n";
        end();
    }
}

void setchar(string letter)//a parameter so this command can be used by the setstring() function
{
    if (type == "CHAR" || type == "STR")
    {
        if (iter > 11 || iter < 0)//incase the user inputs an invalid goto position
        {
            cout << "\n\nERROR: INVALID GOTO VALUE FOR CHARACTER!!!\n\n";
            end();
        }

        int change = (iter * 4);//stores the value that will change the position in the billboard array

    //-------------------------------------------------------
    //LETTERS------------------------------------------------
    //-------------------------------------------------------
        if ((letter[letter.find_first_of('A')]) == 'A')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_A[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('B')]) == 'B')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
                for(int j = 0; j < 4; ++j)//cols
                {
                    billboard[(j + change) + (48 * i)] = char_B[(j + (4 * i))];
                }
            }

                ++iter;
            }
        else if ((letter[letter.find_first_of('C')]) == 'C')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_C[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('D')]) == 'D')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_D[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('E')]) == 'E')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_E[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('F')]) == 'F')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_F[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('G')]) == 'G')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_G[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('H')]) == 'H')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_H[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('I')]) == 'I')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_I[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('J')]) == 'J')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_J[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('K')]) == 'K')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_K[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('L')]) == 'L')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_L[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('M')]) == 'M')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_M[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('N')]) == 'N')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_N[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('O')]) == 'O')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_O[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('P')]) == 'P')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_P[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('Q')]) == 'Q')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_Q[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('R')]) == 'R')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_R[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('S')]) == 'S')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_S[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('T')]) == 'T')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_T[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('U')]) == 'U')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_U[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('V')]) == 'V')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_V[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('W')]) == 'W')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_W[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('X')]) == 'X')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_X[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('Y')]) == 'Y')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_Y[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('Z')]) == 'Z')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_Z[(j + (4 * i))];
               }
            }

            ++iter;
        }

    //-------------------------------------------------------
    //NUMBERS------------------------------------------------
    //-------------------------------------------------------
        else if ((letter[letter.find_first_of('1')]) == '1')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_1[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('2')]) == '2')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_2[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('3')]) == '3')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_3[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('4')]) == '4')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_4[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('5')]) == '5')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_5[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('6')]) == '6')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_6[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('7')]) == '7')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_7[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('8')]) == '8')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_8[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('9')]) == '9')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_9[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else if ((letter[letter.find_first_of('0')]) == '0')
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_0[(j + (4 * i))];
               }
            }

            ++iter;
        }

    //whitespace
        else if (letter[letter.find_first_of(string::npos)] == string::npos)
        {
            for (int i = 0; i < 5; ++i)//rows
            {
               for(int j = 0; j < 4; ++j)//cols
               {
                    billboard[(j + change) + (48 * i)] = char_Space[(j + (4 * i))];
               }
            }

            ++iter;
        }
        else
        {
            cout << "\n\nERROR: INVALID CHARACTER!!\n\n";
        }

        part2 = "";
    }
    else
    {
        cout << "\n\nERROR: WRONG MODE FOR SETCHAR\n\n";
        end();
    }
}

void setstr()
{
    if (type == "STR")
    {
        string sentence = part2;//stores the sentence from part2
        sentence.erase(sentence.begin());//removes quotations from the start
        sentence.erase(sentence.end() - 1);//removes quotations from the end
        //(-1) so that the end is not the position after the last character

        temp = sentence;//modified for scrolling

        string letter;//stores the letters of the sentence
        int length = sentence.length();

        if (length > 11)
        {
            for (int j = 0; j < (length + 1); ++j)
            {
                for (int i = 0; i < 12; i++)
                {
                    letter = temp[i];
                    setchar(letter);
                }
                if (!temp.empty())//the program wont give an error when getting an empty sentence
                {
                    temp.erase(temp.begin());//reases the first char of the sentence to scroll

                    display();//so the billboard is displayed every time a char is removed
                    //could not make it based on the DISPLAY command in the infile
                }
            }
        }
        else
        {
            for (int i = 0; i < 11; i++)
                {
                    letter = temp[i];
                    setchar(letter);
                }
        }

        part2 = "";
    }
    else
    {
        cout << "\n\nERROR: WRONG MODE FOR SETSTR\n\n";
        end();
    }
}
