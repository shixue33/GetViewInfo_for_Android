

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import android.os.Environment;

public class GenerXml {
	FileOutputStream fileoutputstream = null;
	PrintStream printStream = null;
	private String tab = "\t";
	private String filename;
	public GenerXml(String ActivityName, boolean loop) {
		int filenum = 0;
		String fileName = ActivityName;
		
		File dir = new File(Environment.getExternalStorageDirectory()
				+ "/GetInfoFile/");
		String[] dirs = dir.list();
		filenum = dirs.length;
		int num = 0;
		for (String temp : dirs) {
			if (temp.contains(ActivityName)) {
				num = num + 1;
			}
		}
		fileName = ActivityName + "_" + num;

		try {
			fileoutputstream = new FileOutputStream(
					Environment.getExternalStorageDirectory() + "/GetInfoFile/"
							+ (filenum>9?filenum:("0"+filenum)) + "_" + fileName + ".xml");
			filename = (filenum>9?filenum:("0"+filenum)) + "_" + fileName ;
			printStream = new PrintStream(fileoutputstream);
			printStream.println("<?xml version=\"1.0\" encoding=\"utf-8\"?>");
			printStream.println("<Activity>");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void setView() {
		printStream.println(tab + "<View>");
	}

	public void setProperty(String property, Object value) {
		printStream.println(tab + tab + "<" + property + ">"
				+ String.valueOf(value) + "</" + property + ">");
	}

	public void saveView() {
		printStream.println(tab + "</View>");
	}

	public void saveActivity() {
		printStream.println("</Activity>");
		printStream.flush();
		printStream.close();
		try {
			fileoutputstream.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public String getFileName(){
		return filename;
	}
	public static void main(String[] args) {

	}

}
