package main;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.servlet.ServletHolder;
import servlets.AllRequestsServlet;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;

/**
 * @author Alex Bocharov
 *         <p>
 *         Пример кода
 *         <p>
 *         Описание
 */
public class Main {
    public static void main(String[] args) throws Exception {
        AllRequestsServlet allRequestsServlet = new AllRequestsServlet();

        ServletContextHandler context = new ServletContextHandler(ServletContextHandler.SESSIONS);
        context.addServlet(new ServletHolder(allRequestsServlet), "/*");
        //try {
            //String url = "http://127.0.0.1:8332/";
            //String urlParameters = "{\"jsonrpc\": \"1.0\", \"id\":\"curltest\", \"method\": \"getdifficulty\", \"params\": [] }";
            //URL url = new URL("http://127.0.0.1:8332");

            //URLConnection conn = url.openConnection();
            //conn.setHeader("Authorization","bgl_user:12345678");
            //conn.setDoOutput(true);

            //OutputStreamWriter writer = new OutputStreamWriter(conn.getOutputStream());

            //writer.write(urlParameters);
            //writer.flush();

            //String line;
            //BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));

            //while ((line = reader.readLine()) != null) {
              //  System.out.println(line);
            //}
            //writer.close();
            //reader.close();
        //} catch (Exception e) {
          //  e.printStackTrace();
        //}
        Server server = new Server(8080);
        server.setHandler(context);

        server.start();
        System.out.println("Service started.");
        server.join();

    }
}
