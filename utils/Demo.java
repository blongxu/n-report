package com.blongxu.commapi;

import java.io.File;

public class Demo {
	/**
	 * 查询数据
	 */
	public void testQuery() {
		CommapiSDK commapiSDK = new CommapiSDK();
		try {
			String queryURI = "http://xxxx/commapi/api/api/queryData";
			String apiId = "tWCYzlg_";
			String apiKey = "EnXVDUNk";
			String id = "7529975536366387";
			String begin = "0";
			String length = "10";
			String parms = "{\"deviceSerial\":\"\",\"deviceName\":\"\",\"band\":\"\"}";
			String parmsCheck = "{\"deviceSerial\":false,\"deviceName\":false,\"band\":false}";
			queryResult queryResult = commapiSDK.queryData(queryURI, apiId, apiKey, id, begin, length, parms,
					parmsCheck);
			System.out.println(queryResult.getiTotalRecords());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * 执行命令
	 */
	public void testExecuteData() {
		CommapiSDK commapiSDK = new CommapiSDK();
		try {
			String executeURI = "http://xxxx/commapi/api/api/executeData";
			String apiId = "tWCYzlg_";
			String apiKey = "EnXVDUNk";
			String id = "7529975536366387";
			String parms = "[{\"deviceSerial\":\"\",\"deviceName\":\"\",\"band\":\"\"}]";
			ExecuteStatus executeStatus = commapiSDK.executeData(executeURI, apiId, apiKey, id, parms);
			System.out.println(executeStatus.getActionMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void testAddFile() {
		CommapiSDK commapiSDK = new CommapiSDK();
		try {
			String executeURI = "http://xxxx/commapi/api/api/addFiles";
			String apiId = "tWCYzlg_";
			String apiKey = "EnXVDUNk";
			String id = "7529975536366387";
			String parms = "nfile";
			File file = new File("D:\\xxx.xml");
			ExecuteStatus executeStatus = commapiSDK.addFile(executeURI, apiId, apiKey, id, parms, file);
			System.out.println(executeStatus.getActionMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void testDeleteFile() {
		CommapiSDK commapiSDK = new CommapiSDK();
		try {
			String executeURI = "http://xxxx/commapi/api/api/deleteFiles";
			String apiId = "tWCYzlg_";
			String apiKey = "EnXVDUNk";
			String id = "7529975536366387";
			String fileIds = "[\"1111\",\"2222\"]";
			ExecuteStatus executeStatus = commapiSDK.deleteFile(executeURI, apiId, apiKey, id, fileIds);
			System.out.println(executeStatus.getActionMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void testQueryFileByParm() {
		CommapiSDK commapiSDK = new CommapiSDK();
		try {
			String executeURI = "http://xxxx/commapi/api/api/getFileByParms";
			String apiId = "tWCYzlg_";
			String apiKey = "EnXVDUNk";
			String id = "7529975536366327";
			String parms = "nfile";
			String begin = "0";
			String length = "10";
			String beginTime = "2024-01-01";
			String endTime = "2025-01-01";
			ExecuteStatus executeStatus = commapiSDK.getFileByParms(executeURI, apiId, apiKey, id, parms, begin, length,
					beginTime, endTime);
			System.out.println(executeStatus.getActionMessage());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}


}
