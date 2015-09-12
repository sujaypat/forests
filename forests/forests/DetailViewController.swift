//
//  DetailViewController.swift
//  forests
//
//  Created by Sujay Patwardhan on 09/12/2015.
//  Copyright (c) 2015 Sujay Patwardhan. All rights reserved.
//

import UIKit
//import ParseUI

class DetailViewController: UIViewController {
	
	// Container to store the view table selected object
	var currentObject : PFObject?
	
	// Some text fields
	@IBOutlet weak var ticker: UITextField!
	
	
	// The save button
//	@IBAction func saveButton(sender: AnyObject) {
//		
//		// Unwrap the current object object
//		if let object = currentObject {
//            
////            let name = object.valueForKey("name") as! String
//            print(object)
//			
//			object["Ticker"] = objectID.valueForKey("Ticker")
//
//			// Save the data back to the server in a background task
////			object.saveEventually(nil)
//			
//		}
//		
//		// Return to table view
//		self.navigationController?.popViewControllerAnimated(true)
//	}
	
	override func viewDidLoad() {
		super.viewDidLoad()
		print("loaded")
		// Unwrap the current object object
		if let object = currentObject {
			ticker.text = object.valueForKey("Ticker") as? String

		}
	}
	
	
	override func didReceiveMemoryWarning() {
		super.didReceiveMemoryWarning()
		// Dispose of any resources that can be recreated.
	}
	
	
	/*
	// MARK: - Navigation
	
	// In a storyboard-based application, you will often want to do a little preparation before navigation
	override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
	// Get the new view controller using segue.destinationViewController.
	// Pass the selected object to the new view controller.
	}
	*/
	
}
