

import java.io.File;
import java.util.ArrayList;

import android.os.Environment;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.robotium.solo.Solo;

public class GetCurrentInfo {
	private Solo solo;
	public GetCurrentInfo(Solo solo){
		this.solo = solo;
		clearFiles();
	}
	
	public void loopGetInfo(){
		loopGetInfo(5000);
	}
	
	public void loopGetInfo(int time){
		while(true){
			solo.sleep(time);
			getCurrentInfo(true);
		}
	}
	//parameter loop
	public void getCurrentInfo(boolean loop){
		GenerXml gx = new GenerXml(solo.getCurrentActivity().getClass().getSimpleName(),loop);
		ArrayList<View> av = solo.getCurrentViews();
		
		for (View view : av) {
			int id = view.getId();			
			gx.setView();
			gx.setProperty("name", view.getClass().getName());
			if(id!=-1){
				if (null != view.getResources()
						&& null != view.getResources().getResourceEntryName(id)){				
					gx.setProperty("id", view.getResources().getResourceEntryName(id));
					gx.setProperty("resourseId", Integer.toHexString(id));
				}	
			}
			int[] location = { 0, 0 };
			view.getLocationInWindow(location);
			gx.setProperty("x", location[0]);
			gx.setProperty("y", location[1]);
			gx.setProperty("width", view.getWidth());
			gx.setProperty("height", view.getHeight());
			if(null != view.getTag()){
				gx.setProperty("tag", view.getTag());
			}
			if (view instanceof TextView) {
				gx.setProperty("text", ((TextView) view).getText());
			}
			if(view instanceof ViewGroup){
				gx.setProperty("type", "ViewGroup");
			}			
			gx.setProperty("clickable", view.isClickable());
			gx.setProperty("enable", view.isEnabled());
			gx.saveView();
		}
		solo.takeScreenshot(gx.getFileName());
		gx.saveActivity();
		
	}
	
	
	public void clearFiles(){
		File rootDir = new File(Environment.getExternalStorageDirectory()+"/GetInfoFile/");
		File rootDir2 = new File(Environment.getExternalStorageDirectory()+"/Robotium-Screenshots/");
		if (rootDir.exists()) {			
			File[] files = rootDir.listFiles();
			for(File file:files){
				file.delete();
			}
		}else{			
			rootDir.mkdir();
		}
		if (rootDir2.exists()) {			
			File[] files = rootDir2.listFiles();
			for(File file:files){
				file.delete();
			}
		}else{			
			rootDir2.mkdir();
		}
	}

}
