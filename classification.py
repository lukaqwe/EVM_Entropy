# string containing opcodes is taken from Mastering Ethereum, O'reilly

import re
ArithmeticOps = '''ADD        //Add the top two stack items
MUL        //Multiply the top two stack items
SUB        //Subtract the top two stack items
DIV        //Integer division
SDIV       //Signed integer division
MOD        //Modulo (remainder) operation
SMOD       //Signed modulo operation
ADDMOD     //Addition modulo any number
MULMOD     //Multiplication modulo any number
EXP        //Exponential operation
SIGNEXTEND //Extend the length of a two's complement signed integer
SHA3       //Compute the Keccak-256 hash of a block of memory'''

StackMemoryOps = '''POP     //Remove the top item from the stack
MLOAD   //Load a word from memory
MSTORE  //Save a word to memory
MSTORE8 //Save a byte to memory
SLOAD   //Load a word from storage
SSTORE  //Save a word to storage
MSIZE   //Get the size of the active memory in bytes
PUSHx   //Place x byte item on the stack, where x can be any integer from
        // 1 to 32 (full word) inclusive
DUPx    //Duplicate the x-th stack item, where x can be any integer from
        // 1 to 16 inclusive
SWAPx   //Exchange 1st and (x+1)-th stack items, where x can be any
        // integer from 1 to 16 inclusive'''

ProcessFlowOps = '''STOP      //Halt execution
JUMP      //Set the program counter to any value
JUMPI     //Conditionally alter the program counter
PC        //Get the value of the program counter (prior to the increment
          //corresponding to this instruction)
JUMPDEST  //Mark a valid destination for jumps'''

SystemOps = """LOGx          //Append a log record with x topics, where x is any integer
              //from 0 to 4 inclusive
CREATE        //Create a new account with associated code
CALL          //Message-call into another account, i.e. run another
              //accounts code
CALLCODE      //Message-call into this account with another
              //accounts code
RETURN        //Halt execution and return output data
DELEGATECALL  //Message-call into this account with an alternative
              //accounts code, but persisting the current values for
              //sender and value
STATICCALL    //Static message-call into an account
REVERT        //Halt execution, reverting state changes but returning
              //data and remaining gas
INVALID       //The designated invalid instruction
SELFDESTRUCT  //Halt execution and register account for deletion"""


LogicOps = '''LT     //Less-than comparison
GT     //Greater-than comparison
SLT    //Signed less-than comparison
SGT    //Signed greater-than comparison
EQ     //Equality comparison
ISZERO //Simple NOT operator
AND    //Bitwise AND operation
OR     //Bitwise OR operation
XOR    //Bitwise XOR operation
NOT    //Bitwise NOT operation
BYTE   //Retrieve a single byte from a full-width 256-bit word'''

EnvironmentalOps = '''GAS            //Get the amount of available gas (after the reduction for
               //this instruction)
ADDRESS        //Get the address of the currently executing account
BALANCE        //Get the account balance of any given account
ORIGIN         //Get the address of the EOA that initiated this EVM
               //execution
CALLER         //Get the address of the caller immediately responsible
               //for this execution
CALLVALUE      //Get the ether amount deposited by the caller responsible
               //for this execution
CALLDATALOAD   //Get the input data sent by the caller responsible for
               //this execution
CALLDATASIZE   //Get the size of the input data
CALLDATACOPY   //Copy the input data to memory
CODESIZE       //Get the size of code running in the current environment
CODECOPY       //Copy the code running in the current environment to
               //memory
GASPRICE       //Get the gas price specified by the originating
               //transaction
EXTCODESIZE    //Get the size of any account's code
EXTCODECOPY    //Copy any account's code to memory
RETURNDATASIZE //Get the size of the output data from the previous call
               //in the current environment
RETURNDATACOPY //Copy data output from the previous call to memory'''

BlockOps = '''BLOCKHASH  //Get the hash of one of the 256 most recently completed
           //blocks
COINBASE   //Get the block's beneficiary address for the block reward
TIMESTAMP  //Get the block's timestamp
NUMBER     //Get the block's number
DIFFICULTY //Get the block's difficulty
GASLIMIT   //Get the block's gas limit'''

# returns only the mnemonics from the list of strings


def clean(opcodesList):
    mnemonic = re.compile("[A-Z]+[x]?")
    result = []
    for opcode in opcodesList:
        if mnemonic.match(opcode) and opcode != 'Keccak-256':
            if opcode[-1] == 'x':
                result.append(opcode[:-1])
            else:
                result.append(opcode)
    return result


def classify():
    Classes = {"Arithmetic": ArithmeticOps, "Block": BlockOps, "Logic": LogicOps, "System": SystemOps,
               "ProcessFlow":  ProcessFlowOps, "StackMemory":  StackMemoryOps, "Environmental": EnvironmentalOps}

    for key in Classes:
        Classes[key] = clean(Classes[key].split())
    return Classes


if __name__ == "__main__":
    print(classify())
