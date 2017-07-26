LDFLAGS = -Wl,--no-as-needed `libnet-config --libs`
CFLAGS = -ggdb -Wall `libnet-config --defines`

OBJECTS = libnet_tutorial1

all : $(OBJECTS)
clean :
	\rm $(OBJECTS)
.PHONY: all clean

% : %.c
