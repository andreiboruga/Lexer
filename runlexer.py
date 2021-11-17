class DFA:
    def __init__(self, data, name):
        self.name = name
        self.initial_state = data[0]
        self.alphabet = set()
        self.delta = dict()
        for i in range(1, len(data) - 1):
            if data[i][1] == '\\n':
                self.alphabet.add('\n')
                self.delta[(data[i][0], '\n')] = data[i][2]
            else:
                self.alphabet.add(data[i][1])
                self.delta[(data[i][0], data[i][1])] = data[i][2]
        self.final_states = list(data[len(data) - 1].split())

    def get_initial_state(self):
        return self.initial_state

    def get_final_states(self):
        return self.final_states

    def next_config(self, state, rest):
        if (state, rest[0]) in self.delta.keys():
            return self.delta[(state, rest[0])], rest[1::]
        else:
            return False, False

    def get_name(self):
        return self.name

    def accepted(self, word):
        state = self.get_initial_state()
        while (word):
            state, word = self.next_config(state, word)
        if state in self.get_final_states():
            return True
        else:
            return False

def solve(dfas, f, NUMBER_OF_DFAS, fout):
    f2 = open(fout, "w")
    sentence = f
    init_s_len = len(sentence)
    state = []
    accepted_word = []
    for i in range(NUMBER_OF_DFAS):
        state.append(dfas[i].get_initial_state())
        accepted_word.append('')

    indice = 0
    max_word_len = 1
    while (sentence and max_word_len):
        indice = 0
        sentence_copy = sentence
        while (sentence_copy):
            all_f = True
            for i in range(NUMBER_OF_DFAS):
                state[i], aux = dfas[i].next_config(state[i], sentence_copy)
                if state[i] != False:
                    all_f = False
                if state[i] in dfas[i].get_final_states():
                    accepted_word[i] = sentence[:indice + 1:1]
            sentence_copy = sentence_copy[1::]
            if all_f:
                break
            indice += 1

        max_word_len = 0
        the_accepted_word = ''
        token = None
        for i in range(NUMBER_OF_DFAS):
            if len(accepted_word[i]) > max_word_len:
                max_word_len = len(accepted_word[i])
                the_accepted_word = accepted_word[i]
                token = dfas[i].get_name()
            accepted_word[i] = ''
            state[i] = dfas[i].get_initial_state()

        if token == None:
            f2.close()
            open(fout, "w").close()
            f2 = open(fout, "w")
            if indice >= len(sentence):
                f2.write("No viable alternative at character EOF, line 0")
            else:
                f2.write("No viable alternative at character " + (init_s_len - len(sentence) + indice).__str__() + ", line 0")
            f2.close()
            return

        if the_accepted_word == '\n':
            f2.write(token + " \\n" + '\n')
        else:
            f2.write(token + " " + the_accepted_word + "\n")

        sentence = sentence[max_word_len::]

    f2.close()

def runlexer(lexer, fin, fout):
    NUMBER_OF_DFAS = 0
    dfas = []

    f1 = open(lexer, "r").read().split(sep='\n')
    while f1:
        aux = f1[0]
        i = 1
        name = f1[i]
        i += 1
        data = []
        data.append(f1[i])
        i += 1
        while i < len(f1) and f1[i] != '':
            data.append(f1[i])
            i += 1

        for j in range(1, len(data) - 1):
            # if data[j][3] == '\\' and  data[j][4] == 'n':
            #     data[j] = [data[j][0], data[j][3] + data[j][4], data[j][7]]
            #     continue
            data[j] = list(data[j].split(sep=','))
            data[j][1] = data[j][1][1:len(data[j][1]) - 1:1]

        f1 = f1[i + 1::]
        # print(data)
        dfas.append(DFA(data, name))
        NUMBER_OF_DFAS += 1

    # print(dfas[1].alphabet)
    # print(NUMBER_OF_DFAS)

    f = open(fin, "r").read()
    solve(dfas, f, NUMBER_OF_DFAS, fout)

