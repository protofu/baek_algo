import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		OutputStream outputStream = new BufferedOutputStream(System.out);

		int[] arr = new int[10001];

		int n = Integer.parseInt(reader.readLine());
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(reader.readLine());
			arr[num]++;
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 10001; i++) {
			for (int j = 0; j < arr[i]; j++) {
				sb.append(i).append('\n');
			}
		}
		outputStream.write(sb.toString().getBytes());
		outputStream.flush();
		outputStream.close();
		reader.close();
	}

}