CXX = g++
CXXFLAGS = -Wall -g
RM = rm -f
DNC = DivideAndConquer/
GRD = Greedy/
DYP = DynamicProgramming/
TST = Test/

run : 
	./src
# build: Main
# cbuild: clean Main 
build: compile run

compile: src.o $(TST)test.o $(DNC)dnc.o $(GRD)greedy.o $(DYP)dp.o
	$(CXX) $(CXXFLAGS)  src.o $(DNC)dnc.o $(TST)test.o $(GRD)greedy.o $(DYP)dp.o -o src 

src.o : src.cpp
	$(CXX) $(CXXFLAGS) -c src.cpp -o src.o

$(TST)%.o: $(TST)%.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

$(DNC)%.o: $(DNC)%.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

$(GRD)%.o: $(GRD)%.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

$(DYP)%.o: $(DYP)%.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@
clean:
	$(RM) src src.o $(TST)test.o $(DNC)dnc.o $(GRD)greedy.o $(DYP)dp.o