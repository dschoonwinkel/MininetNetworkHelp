import java.io.*;
import java.net.*;

class UDPSender {
  public static void main(String args[]) throws Exception {
    DatagramSocket clientSocket = new DatagramSocket();
    InetAddress IPAddress = InetAddress.getByName("10.0.0.2");
    String text = "Hello World!";
    DatagramPacket sendPacket = new DatagramPacket(text.getBytes(), text.length(), IPAddress, 9000);
    clientSocket.send(sendPacket);
    clientSocket.close();
    
  }
}