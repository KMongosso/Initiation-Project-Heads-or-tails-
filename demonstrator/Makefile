#Compiler and options 
CXX=g++
CXXFLAGS=-Wall -ansi -pedantic -Wextra
#Headers path 
HDPATH=headers

SRCS=src/demonstrator.cpp src/display.cpp src/predictors.cpp src/main.cpp
OBJS=$(SRCS:.cpp=.o)

#Final target
EXEC=demonstrator.exe

all: $(EXEC) .depend 

$(EXEC): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)
%.o: %.cpp
	$(CXX) -I$(HDPATH) $(CXXFLAGS) -o $@ -c $<

#Dependences in headers for the .cpp 
.depend: $(SRCS)
	gcc -I$(HDPATH) -MM $(SRCS) > $@

include .depend

.PHONY: clean rmproper

clean: 
	rm -rf ./src/*.o
rmproper: clean
	rm -rf $(EXEC)
