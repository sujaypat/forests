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
//		self.parseClassName = "BloombergObject"
//		self.textKey = "Ticker"
//		self.pullToRefreshEnabled = false
//		self.paginationEnabled = false
	}
    
    
//    var arr : NSMutableArray = []
    
    override func viewWillAppear(animated: Bool) {
        loadObjects()
    }
    
    override func queryForTable() -> PFQuery {
        let query = BloombergObject.query()
        return query!
    }
	

	//override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell
//    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath, object: PFObject!) -> PFTableViewCell? {
//        // 1
//        let cell = tableView.dequeueReusableCellWithIdentifier("Cell", forIndexPath: indexPath) as! TableViewCell
//        
//        // 2
//        let bloomEntry = object as! BloombergObject
//        
//        
//        // 4
//        let name = bloomEntry.Name
//        
//        print(name)
//        
//        cell.textLabel!.text = "\(name)"
//        
//        return cell
//    }
	
	// In a storyboard-based application, you will often want to do a little preparation before navigation
	override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
		
		// Get the new view controller using [segue destinationViewController].
//		let detailScene = segue.destinationViewController as? DetailViewController
//		
//		// Pass the selected object to the destination view controller.
//		if let indexPath = self.tableView.indexPathForSelectedRow {
//			let row = Int(indexPath.row)
//			detailScene?.currentObject = (objects?[row] as! PFObject)
//		}
	}
	
	override func viewDidAppear(animated: Bool) {
		
		// Refresh the table to ensure any data changes are displayed
		tableView.reloadData()
	}
	
}
