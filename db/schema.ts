import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';
export const users=sqliteTable('users',{id:text('id').primaryKey(),name:text('name').notNull(),bio:text('bio').notNull().default(''),avatar:text('avatar').notNull().default(''),created:integer('created').notNull()});
export const configuration=sqliteTable('configuration',{key:text('key').primaryKey(),value:text('value').notNull()});
export const submissions=sqliteTable('submissions',{id:text('id').primaryKey(),uid:text('uid').notNull(),pid:integer('pid').notNull(),language:text('language').notNull(),code:text('code').notNull(),status:text('status').notNull(),detail:text('detail').notNull().default(''),passed:integer('passed').notNull().default(0),total:integer('total').notNull().default(0),created:integer('created').notNull()});
export const accepted=sqliteTable('accepted',{key:text('key').primaryKey(),uid:text('uid').notNull(),pid:integer('pid').notNull(),coins:integer('coins').notNull(),created:integer('created').notNull()});
export const personal=sqliteTable('personal',{uid:text('uid').primaryKey(),body:text('body').notNull()});
export const customProblems=sqliteTable('custom_problems',{id:integer('id').primaryKey({autoIncrement:true}),body:text('body').notNull()});
