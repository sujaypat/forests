//
//  TableViewController.swift
//  forests
//
//  Created by Sujay Patwardhan on 09/12/2015.
//  Copyright (c) 2015 Sujay Patwardhan. All rights reserved.
//

import UIKit

class TableViewController: PFQueryTableViewController {

	// Initialise the PFQueryTable tableview
	override init(style: UITableViewStyle, className: String!) {
		super.init(style: style, className: className)
	}
	
	required init!(coder aDecoder: NSCoder) {
		super.init(coder: aDecoder)
  
		// Configure the PFQueryTableView
		self.parseClassName = "BloombergObject"
		self.textKey = "Ticker"
		self.pullToRefreshEnabled = false
		self.paginationEnabled = false
	}
    
    
    var arr : NSMutableArray = []
    
	
	// Define the query that will provide the data for the table view
	override func queryForTable() -> PFQuery {
        let query:PFQuery = PFQuery(className: "BloombergObject")
		query.orderByAscending("Ticker")
        print(query)
        print ("sdfilbfblirdneirnbrevdvsfdbrb")
        print(query.getObjectWithId("Ticker"))
        query.findObjectsInBackgroundWithBlock{ (objects,error) -> Void in
            if error == nil {
                for object in objects! {
                    self.arr.addObject(object)
                }
            }
        }
        return query
	}
    
	//override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell
	override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath, object: PFObject?) -> PFTableViewCell {
		
        var cell = PFTableViewCell()
        

            print("c,vzxbcv,mnzcxbv,mnbzxc,mvnbcx,mnvbxzc,mvbxzc,mnvb")
            cell = tableView.dequeueReusableCellWithIdentifier("Cell") as! PFTableViewCell!
            if (cell as UITableViewCell? == nil) {
                cell = PFTableViewCell(style: UITableViewCellStyle.Default, reuseIdentifier: "Cell")
            }
            //        cell.textLabel!.text = "usdj"
            
            // Extract values from the PFObject to display in the table cell
            if let ID = queryForTable().valueForKey("Ticker") as? String {
                cell.textLabel!.text = ID
                print("id" + ID)
            }
        
        
        
//        if let displayIntake = PFUser.currentUser()!["IntakeCode"] as? String {
//            txtIntake.text = displayIntake
//        }
        
//        let name = object!.valueForKey("ObjectId") as! String
//        print(name)
        
//        print(object!.valueForKey("ObjectId") as! String)
//		if let capital = object?["capital"] as? String {
//			cell?.detailTextLabel?.text = capital
//		}
		
		return cell
	}
	
	// In a storyboard-based application, you will often want to do a little preparation before navigation
	override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
		
		// Get the new view controller using [segue destinationViewController].
		let detailScene = segue.destinationViewController as? DetailViewController
		
		// Pass the selected object to the destination view controller.
		if let indexPath = self.tableView.indexPathForSelectedRow {
			let row = Int(indexPath.row)
			detailScene?.currentObject = (objects?[row] as! PFObject)
		}
	}
	
	override func viewDidAppear(animated: Bool) {
		
		// Refresh the table to ensure any data changes are displayed
		tableView.reloadData()
	}
	
}
