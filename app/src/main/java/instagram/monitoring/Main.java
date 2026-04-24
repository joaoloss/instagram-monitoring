package instagram.monitoring;

import io.github.cdimascio.dotenv.Dotenv;
import org.asynchttpclient.AsyncHttpClient;
import org.asynchttpclient.DefaultAsyncHttpClient;

public class Main {
    public static void main(String[] args) throws Exception {
        Dotenv dotenv = Dotenv.load();

        String rapidApiKey = dotenv.get("RAPIDAPI_KEY");
        if (rapidApiKey == null || rapidApiKey.isBlank()) {
            rapidApiKey = System.getenv("RAPIDAPI_KEY");
        }

        if (rapidApiKey == null || rapidApiKey.isBlank()) {
            throw new IllegalStateException("Missing RAPIDAPI_KEY. Set it in app/.env or as an environment variable.");
        }

        AsyncHttpClient client = new DefaultAsyncHttpClient();
        client.prepare("GET", "https://instagram-looter2.p.rapidapi.com/reels?id=266439562&count=2")
            .setHeader("x-rapidapi-key", rapidApiKey)
            .setHeader("x-rapidapi-host", "instagram-looter2.p.rapidapi.com")
            .execute()
            .toCompletableFuture()
            .thenAccept(System.out::println)
            .join();

        client.close();
    }
}

// virginia ID: 266439562